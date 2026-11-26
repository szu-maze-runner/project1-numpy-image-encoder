# Project 1：用 NumPy 复现 OpenCLIP ViT-B-32 图像编码器

**GitHub 仓库（Public，助教与老师可访问）**：https://github.com/szu-maze-runner/project1-numpy-image-encoder

> 课程小项目：给定 10 张图像与训练好的参数 theta，**只用 NumPy** 手写 Vision Transformer 的
> 前向计算，把每张图像编码成一个 512 维、单位长度的数值特征，并与独立 Torch FP32 参考结果对齐。
> 本项目不需要训练、不需要 GPU、不需要 PyTorch / OpenCLIP 包，也不需要联网。

**本次提交内容**：补全后的 `image_encoder.py`（TODO-01 ~ TODO-06）、本 README、
`requirements.txt`、`results/` 下的真实校验结果与输出特征、`report/` 下的实验报告，
以及保留在 Git 历史中的多次真实提交。课程原始英文说明另存于 `docs/COURSE-README.md`。

---

## 1. 任务与数据流

| 环节 | 输入 → 输出 shape | 说明 |
| --- | --- | --- |
| 预处理（已提供） | 图片 → `[B,3,224,224]` | 双三次最短边缩放 + 中心裁剪 + OpenCLIP 均值/方差归一化 |
| `patchify` | `[B,3,224,224]` → `[B,49,3072]` | 7×7 个 32×32 patch，块内按 C,H,W 展开 |
| `embed` | → `[B,50,768]` | 无偏置 patch 投影 → 前置 CLS → 加可学习位置向量 |
| `pre_norm` + 12×`TransformerBlock` | → `[B,50,768]` | 每层含 Norm1/多头注意力/残差、Norm2/GELU MLP/残差 |
| `__call__` | → `[B,512]` | 取 CLS → `ln_post` → `visual.proj` → 单位化 |

- **输入**：`float32 [B,3,224,224]`，由 `preprocess_image.py` 生成；`B` 可为任意批量大小。
- **内部序列**：`last_tokens` 为 `float32 [B,50,768]`（CLS + 49 个 patch token）。
- **最终输出**：`output_tokens`，`float32 [B,512]`，每张图一行且 L2 范数为 1；
  `run.py` 按输入顺序把图像 ID 与特征一起保存。
- 模型为固定 checkpoint（ViT-B-32：width 768、12 heads、head_dim 64、12 layers、MLP 3072），
  参数全部来自 `weights/image_encoder.npz` 的 152 个视觉张量；`config.json` 只是结构描述，
  改数字不会变成另一个模型。

## 2. 仓库结构

| 路径 | 职责 | 本次是否编写 |
| --- | --- | --- |
| `image_encoder.py` | **核心实现**：`MultiHeadAttention` / `TransformerBlock` / `ImageEncoder` | 是（补全 6 组 TODO） |
| `helpers.py` | LayerNorm、精确 GELU(erf)、softmax 系数、causal mask、单位化 | 否，课程提供 |
| `preprocess_image.py` | resize / center crop / CHW 归一化 | 否，课程提供 |
| `runtime.py` | 权重、图片、JSON 的加载（路径相对脚本所在目录） | 否，课程提供 |
| `run.py` | 命令行入口：图片 → `[B,512]` → `npz` | 否，课程提供 |
| `check.py` | 8 个阶段的数值校验（唯一读取参考数组的地方） | 否，课程提供 |
| `transformer_steps.py` | 课堂配套：3 token / 4 特征的迷你 Transformer 计算演示 | 否，课程提供 |
| `config.json` | 结构与归一化常数 | 否，课程提供 |
| `requirements.txt` | 依赖清单：`numpy>=1.24,<3`、`Pillow>=9.2,<13`、`imageio>=2.31,<3` | 否，课程提供（本次核对） |
| `assets/images/*.jpg`、`assets/images.json` | 10 张本地图片、稳定 ID、SHA-256 与来源出处 | 否，课程提供（随仓库提交） |
| `weights/manifest.json` | 152 个张量的名字、shape、dtype、SHA-256 指纹 | 否，课程提供 |
| `PPT-CODE-MAP.txt`、`SOURCE-MANIFEST.json` | 课件 76 页与源码对照、文件溯源 | 否，课程提供 |
| `lecture-demos/`、`practice/` | 课堂示例与 12 道 NumPy 练习题（不含课件答案） | 否，课程提供 |
| `docs/COURSE-README.md` | 课程发放的原始英文 README 备份 | 是（整理归档） |
| `results/` | 本次实测的误差记录、输出特征与图 | 是 |
| `report/` | 实验报告（官方模板 PDF + Word + Markdown，含可编译 LaTeX 源） | 是 |
| `SUBMISSION.md` | GitHub 与畅课平台的提交操作步骤 | 是 |
| `.gitignore` | 排除超大权重、参考输出与缓存 | 是 |

## 3. 必要数据及获取方法（重要）

GitHub 单文件上限 100 MB，而 `weights/image_encoder.npz` 为 **326,388,585 字节（约 311 MiB）**，
因此**课程发放的两个大文件不随仓库提交**，请按下述方法取得；助教/老师复现时同样操作即可：

1. 从课程附件 `project1-numpy-student/` 复制
   `weights/image_encoder.npz` → 本仓库 `weights/` 目录；
   复制 `assets/reference_outputs.npz` → 本仓库 `assets/` 目录。
2. 其余小文件（10 张图片、`config.json`、两个 `manifest.json`、`images.json`）已随仓库提交。
3. 校验完整性（可选）：

   ```bash
   python -c "import hashlib,json; from pathlib import Path; m=json.load(open('weights/manifest.json',encoding='utf-8')); print(hashlib.sha256(Path('weights/image_encoder.npz').read_bytes()).hexdigest()==m['weights_sha256']); a=json.load(open('assets/manifest.json',encoding='utf-8')); print(hashlib.sha256(Path('assets/reference_outputs.npz').read_bytes()).hexdigest()==a['reference_sha256'])"
   ```

   两句都应为 `True`；`check.py --stage assets` 也会自动校验全部 152 个张量、10 张图与参考文件。
4. 若确需把权重放进仓库，请使用 Git LFS：`git lfs install && git lfs track "weights/*.npz"`，
   并在提交前确认 `.gitattributes` 已随仓库提交。本次采用「课程附件获取」方式。

`reference_outputs.npz` **仅被 `check.py` 读取**，绝不作为编码器输入；实现不得缓存参考行，
且必须能处理其它图片与不同批量大小。

## 4. 环境与运行步骤（可复现）

- 实测环境：Windows 11 / Python 3.14.3 / NumPy 2.4.3 / Pillow 12.3.0；
  课程要求 Python ≥ 3.9，无需 GPU、无需联网。
- 全部命令在仓库根目录执行；脚本按自身所在目录解析权重与图片路径。

```bash
python -m pip install -r requirements.txt          # 依赖清单
python transformer_steps.py                        # 课堂迷你计算演示（可选）
python check.py --stage assets                     # 校验权重/图片指纹
python check.py --stage patches                    # 建议按阶段逐个排查
python check.py --stage tokens
python check.py --stage block0
python check.py --stage last_tokens
python check.py --stage output
python check.py --stage batch                      # 乱序 + 重复图片
python check.py --stage all                        # 一次性跑完 8 个阶段
python run.py --output results/output_tokens.npz   # 导出 10 张图的 [10,512] 特征
python run.py --images a.jpg b.png --output my.npz  # 自定义图片
```

`check.py --stage all` 在实测机器上约需 **2 分 13 秒**：瓶颈是课程提供的
`helpers.GELU` 用 Python 循环逐元素调用 `math.erf`（详见报告「局限与改进」）。

## 5. 数值校验结果（本机真实输出）

判定：`abs(actual-reference) <= atol + rtol*abs(reference)`，且 shape / `float32` / 有限值全部通过。

| 阶段 | shape | max_abs | mean_abs | atol | rtol | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| preprocess | (10,3,224,224) | 0.000e+00 | 0.000e+00 | 2e-6 | 2e-4 | PASS |
| patches | (2,49,3072) | 0.000e+00 | 0.000e+00 | 2e-4 | 2e-4 | PASS |
| tokens | (2,50,768) | 4.005e-05 | 1.289e-06 | 2e-4 | 2e-4 | PASS |
| block0 | (2,50,768) | 7.063e-06 | 3.250e-07 | 2e-4 | 2e-4 | PASS |
| last_tokens | (2,50,768) | 4.768e-05 | 2.696e-06 | 2e-4 | 2e-4 | PASS |
| output | (10,512) | 5.439e-07 | 8.306e-08 | 2e-5 | 2e-4 | PASS |
| batch | (3,512) | 4.619e-07 | 7.632e-08 | 2e-5 | 2e-4 | PASS |

`output` / `batch` 两阶段还额外检查了每行 L2 范数为 1。原始记录见
`results/check_log.txt`、`results/check_errors.csv`。

## 6. 实现要点（6 组 TODO）

1. **TODO-01 `patchify`**：`reshape(B,3,7,32,7,32).transpose(0,2,4,1,3,5)` 把网格轴移到前面，
   再展平成 `[B,49,3072]`，保证 patch 行优先、块内 C,H,W 顺序与 `conv1.weight` 一致。
2. **TODO-02 `split_heads`**：`[B,N,768] → reshape(B,N,12,64) → transpose(0,2,1,3) → [B,12,N,64]`，
   token 顺序不变。
3. **TODO-03 注意力**：`scores = (q @ k.transpose(0,1,3,2)) / sqrt(64)`（**只换 k 的最后两轴**）；
   `context = softmax(scores) @ v`；`transpose(0,2,1,3).reshape(B,N,768)` 精确还原切分；
   输出投影用 `out_weight.T`（权重为 `[out,in]`）。
4. **TODO-04 残差**：第一条残差加在原始 `x` 上（不是 `norm1(x)`）；MLP 为
   `GELU(u @ W1.T + b1) @ W2.T + b2`，第二条残差加在 `residual` 上。
5. **TODO-05 `embed`**：`patches @ patch_weight.T`（**无偏置**）→ 拼接 CLS → 加 `[50,768]` 位置向量。
6. **TODO-06 输出**：取 `tokens[:,0,:]` → `post_norm` → `@ visual.proj`（该矩阵已是 `[in,out]`，
   **不转置**）→ `unit_vector`。

## 7. 本人贡献与使用的协助

- **独立完成**：`image_encoder.py` 中 6 组 TODO 的全部实现、shape 推导与多头组织；
  分阶段调试与 8 项数值校验；本 README、`results/` 证据、`report/` 实验报告与提交指南的撰写。
- **课程提供、未改动**：`helpers.py`、`preprocess_image.py`、`runtime.py`、`run.py`、
  `check.py`、`transformer_steps.py`、权重与参考输出、10 张图片、课件对照表。
- **协助**：课堂幻灯片 39–73 页、`PPT-CODE-MAP.txt` 与 `transformer_steps.py` 用于确认计算顺序；
  AI 助手用于代码审阅、文档排版与文字润色，未用于生成或缓存参考数值。

## 8. 与期末项目的衔接

把补全后的 `image_encoder.py` **连同课程提供的 `helpers.py`** 复制到期末项目附件中
`clip.py` / `text_encoder.py` 所在目录即可复用：`ImageEncoder(weights)`、`LayerNorm`、
`TransformerBlock(weights, prefix, heads)` 的 API 保持一致；可选的 `causal` 开关为后续文本塔保留。
期末项目会使用完整图文 checkpoint，不能用本项目的纯视觉权重替代。
