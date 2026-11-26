"""Student implementation of the final project's image encoder.

Complete TODO-01 through TODO-06 using NumPy. Model parameters are supplied.
The public classes retain the final project's interface. helpers.py is provided.
"""
import numpy as np
from helpers import LayerNorm, GELU, attention_weights, causal_mask, unit_vector


class MultiHeadAttention:
    def __init__(self, weights, prefix, heads):
        self.qkv_weight = weights[prefix + '.in_proj_weight']  # [3D,D]
        self.qkv_bias = weights[prefix + '.in_proj_bias']      # [3D]
        self.out_weight = weights[prefix + '.out_proj.weight']  # [D,D]
        self.out_bias = weights[prefix + '.out_proj.bias']
        self.heads = heads
        self.width = self.out_bias.shape[0]
        self.head_dim = self.width // heads

    def split_heads(self, x):
        """TODO-02. Input [B,N,D], return [B,H,N,D/H].

        In this image model D=768, H=12 and D/H=64. Use reshape/transpose.
        Research the head organization independently. Preserve token order.
        """
        B, N, D = x.shape
        assert D == self.width == self.heads * self.head_dim, 'unexpected feature width'
        # Keep the token axis N in front of the head dimension before the swap,
        # so that each head receives 64 consecutive feature channels.
        return x.reshape(B, N, self.heads, self.head_dim).transpose(0, 2, 1, 3)

    def __call__(self, x, causal=False):
        # Given: stored linear weights use [out,in]. Parameters stay fixed.
        qkv = x @ self.qkv_weight.T + self.qkv_bias
        q = self.split_heads(qkv[:, :, :self.width])
        k = self.split_heads(qkv[:, :, self.width:2*self.width])
        v = self.split_heads(qkv[:, :, 2*self.width:])

        # TODO-03a: one score table per batch item and per head, [B,H,N,N].
        # Only the last two axes of k are swapped; batch/head axes stay in place.
        scale = np.sqrt(np.float32(self.head_dim))
        scores = (q @ k.transpose(0, 1, 3, 2)) / scale

        # Given for later text-encoder compatibility. Images use causal=False.
        if causal:
            scores = causal_mask(scores)
        coefficients = attention_weights(scores)  # supplied numerical helper

        # TODO-03b: each query row becomes a weighted mixture of value rows.
        context = coefficients @ v                       # [B,H,N,D/H]
        B, N = context.shape[0], context.shape[2]
        # Undo split_heads exactly: [B,H,N,D/H] -> [B,N,H,D/H] -> [B,N,D].
        merged = context.transpose(0, 2, 1, 3).reshape(B, N, self.width)

        # TODO-03c: stored linear weights are [out,in], hence weight.T.
        return merged @ self.out_weight.T + self.out_bias


class TransformerBlock:
    def __init__(self, weights, prefix, heads):
        self.norm1 = LayerNorm(weights[prefix+'.ln_1.weight'], weights[prefix+'.ln_1.bias'])
        self.norm2 = LayerNorm(weights[prefix+'.ln_2.weight'], weights[prefix+'.ln_2.bias'])
        self.attention = MultiHeadAttention(weights, prefix+'.attn', heads)
        self.fc1_weight = weights[prefix+'.mlp.c_fc.weight']  # [4D,D]
        self.fc1_bias = weights[prefix+'.mlp.c_fc.bias']
        self.fc2_weight = weights[prefix+'.mlp.c_proj.weight']  # [D,4D]
        self.fc2_bias = weights[prefix+'.mlp.c_proj.bias']
        self.gelu = GELU()

    def __call__(self, x, causal=False):
        # Given: normalize each token and calculate its attention update.
        update = self.attention(self.norm1(x), causal=causal)

        # TODO-04a: residual path keeps the original x, not norm1(x).
        residual = x + update

        # Given: the second Norm and the exact checkpoint activation helper.
        u = self.norm2(residual)

        # TODO-04b: two linear layers with the exact supplied GELU in between.
        hidden = u @ self.fc1_weight.T + self.fc1_bias       # [B,N,3072]
        activated = self.gelu(hidden)
        mlp_update = activated @ self.fc2_weight.T + self.fc2_bias  # [B,N,768]
        return residual + mlp_update


class ImageEncoder:
    def __init__(self, weights):
        self.patch_weight = weights['visual.conv1.weight'].reshape(768, 3072)
        self.cls = weights['visual.class_embedding'].reshape(1, 1, 768)
        self.position = weights['visual.positional_embedding']  # [50,768]
        self.pre_norm = LayerNorm(weights['visual.ln_pre.weight'], weights['visual.ln_pre.bias'])
        self.blocks = [TransformerBlock(weights, 'visual.transformer.resblocks.' + str(i), 12)
                       for i in range(12)]
        self.post_norm = LayerNorm(weights['visual.ln_post.weight'], weights['visual.ln_post.bias'])
        self.projection = weights['visual.proj']  # [768,512], already [in,out]

    def patchify(self, images):
        """TODO-01. [B,3,224,224] -> [B,49,3072].

        Visit patches left to right, then top to bottom. Within a patch, flatten
        C,H,W in that order. Each 32x32 RGB patch contributes 3*32*32 values.
        Use reshape/transpose. Do not resize the already-prepared input.
        """
        B, C, H, W = images.shape
        p = 32
        grid = H // p
        assert C == 3 and H == W == 224 and grid * p == H, 'expected [B,3,224,224]'
        # [B,3,224,224] -> [B,3,7,32,7,32] -> [B,7,7,3,32,32].
        # Grid axes come first so patches are row-major (left to right, top down),
        # while the flattened values of each patch stay in C,H,W order.
        x = images.reshape(B, C, grid, p, grid, p).transpose(0, 2, 4, 1, 3, 5)
        return x.reshape(B, grid * grid, C * p * p)

    def embed(self, images):
        patches = self.patchify(images)  # [B,49,3072]

        # TODO-05a: patch_weight is [768,3072] ([out,in]); no bias is used.
        projected = patches @ self.patch_weight.T           # [B,49,768]

        # Given: one supplied CLS row per image.
        cls = np.tile(self.cls, (images.shape[0], 1, 1))

        # TODO-05b: CLS is token 0, patches follow; positions add over the batch.
        tokens = np.concatenate((cls, projected), axis=1)  # [B,50,768]
        return tokens + self.position[None, :, :]

    def encode_tokens(self, images):
        """Provided assembly of token input and the 12 blocks; [B,50,768]."""
        x = self.pre_norm(self.embed(images))
        for block in self.blocks:
            x = block(x)
        return x

    def __call__(self, images):
        """TODO-06. Return one normalized output token [B,512] per image."""
        tokens = self.encode_tokens(images)

        # TODO-06: CLS is row 0; post_norm uses its own separate parameters.
        cls_token = tokens[:, 0, :]                        # [B,768]
        normalized = self.post_norm(cls_token)
        # visual.proj is already [in,out] = [768,512], so there is no transpose.
        output = normalized @ self.projection             # [B,512]

        return unit_vector(output)
