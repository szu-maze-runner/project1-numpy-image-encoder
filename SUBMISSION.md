# 提交状态与最后两步（Project 1 · NumPy 图像编码器）

## 一、已完成（无需你操作）

- **公开仓库已创建并推送**：https://github.com/szu-maze-runner/project1-numpy-image-encoder
  （Public，助教与老师可直接访问；`main` 分支，保留多条真实提交，未 squash / force push）。
- 仓库内含：补全的 `image_encoder.py`、中文 `README.md`、`requirements.txt`、`config.json`、
  课程提供的可运行脚本、10 张小图与指纹清单、`results/`（校验日志、误差表、证据图、输出特征、
  相似度矩阵）、`report/`（官方模板版报告 + Word 版报告 + md）、`.gitignore`。
- **报告已改用学院官方实验报告模板**：`D:\桌面\main.tex` + `D:\桌面\figs\vit_overview.png`
  是深大人工智能学院的 `Experiment-Report-Template-SZU`（11 月 25 日首发），封面预填
  「Python程序设计 / 人工智能学院 / 指导教师 舒婷」，示例插图正是 ViT 架构图，可确认就是本次项目模板。
  用本机 MiKTeX XeLaTeX 编译，保留封面页、五个正文章节与教师批阅/成绩评定页，
  **共 5 页（封面 1 + 正文 3 + 批阅 1）**，无溢出、无乱码，满足「正文 ≤ 5 页」。
- **仓库地址已填好**：README、两份报告、提交说明中均已写入，无需再复制粘贴。
- 326 MB 权重与参考输出按 GitHub 单文件上限排除，README 第 3 节写明获取方式与 SHA-256 校验。

## 二、你要交哪一个

| | 文件 | 说明 |
| --- | --- | --- |
| **推荐** | `report/实验报告-官方模板.pdf` | 学院官方 LaTeX 模板，5 页，直接交 PDF；封面只剩 3 处空栏 |
| 备选 | `report/实验报告.docx` | Word 版，方便在 Word/WPS 里直接编辑填写；5 页 |

两份内容一致，任选其一即可，**不要都交**。若畅课只收 Word，交 docx；若收 PDF 或不限，交官方模板 PDF 更贴合老师预期。

## 三、你只剩两步

1. **填封面信息**：
   - 交 PDF 版：封面「专业、报告人、学号」三处为空，用 WPS/Word 打开 PDF 填入并保存；
     或把三项信息发给我，我重新编译出填好的终版 PDF（1 分钟）。
   - 交 docx 版：把封面「课程名称、学院、专业、指导教师、报告人、学号」六处 `（填写）` 换成真实信息。
   - 项目名称、实验/提交时间、指导教师（舒婷）、GitHub 地址都已填好，不用改。
2. **交到畅课平台**：登录畅课 → 本小项目提交入口 → 上传报告 →
   提交框粘贴 `https://github.com/szu-maze-runner/project1-numpy-image-encoder` →
   刷新确认状态为「已提交」。

若平台强制要求另用官方 docx 模板，可打开 `report/实验报告.md`，按「第 1~4 页」各节依次粘贴，
粘贴后**预览确认总页数仍 ≤ 5 页**。

## 四、可编辑源文件（可选）

`report/official-template/main.tex` 是填好内容的 LaTeX 源，`figs/` 是两张配图。
本机重新编译（在 `report/official-template` 目录下执行两遍，tikz 批阅页需要第二遍定位）：

```bash
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

放到 Overleaf 编译时，把 `\setCJKmainfont[AutoFakeBold=2]{SimSun}` 改回模板原设置
`\setCJKmainfont{Noto Serif CJK SC}`，并选择 XeLaTeX 引擎。

## 五、验收清单

- [x] `image_encoder.py` 6 组 TODO 全部实现，无 `NotImplementedError`
- [x] `python check.py --stage all` 8 个阶段全 PASS（原始日志 `results/check_log.txt`）
- [x] README.md 说明代码功能、结构、依赖、数据获取与运行步骤
- [x] GitHub 仓库为 Public，能看到多条真实 commit，仓库体积只有几 MB
- [x] 报告 ≤ 5 页，含任务与方法、实现要点、可复现性、结果证据、分析反思、本人贡献，并已填入仓库地址
- [x] 已改用学院官方实验报告模板（含教师批阅页）
- [ ] 封面个人信息已填写
- [ ] 畅课平台已上传报告并粘贴仓库地址
- [ ] 没有在最后一刻提交；不接受无理由迟交

## 六、规则提醒（来自截图）

- 成绩构成：**代码 30 分 + 报告 70 分**；本小项目占最终成绩的 **10%**。
- 报告**超过 5 页将得 60 分以下**；两份报告均为 5 页，若粘贴到别的模板请重新预览页数。
- 评分看内容四项（任务与方法、可复现性、结果与证据、分析与反思），模板本身可按需调整；
  官方模板注释亦写明「报告内的项目或内容设置，可根据实际情况加以调整和补充」。
- 迟交 N 天，最终得分 = 批改得分 × (1 − 0.1·N)；有疑问及时请教助教或老师。

## 七、常见问题

| 现象 | 处理 |
| --- | --- |
| 助教说缺权重文件 | 按 README 第 3 节从课程附件复制 `weights/image_encoder.npz` 与 `assets/reference_outputs.npz` 到对应目录（GitHub 单文件限 100 MB） |
| 平台只收 Word | 交 `report/实验报告.docx`；或 Word/WPS 打开官方模板 PDF 另存为 docx |
| 想再跑一次验证 | `python -m pip install -r requirements.txt` 后 `python check.py --stage all`（约 2 分钟） |
| 想改成私有并邀请助教 | 仓库 Settings → 改 visibility 为 Private → Collaborators 添加助教与老师账号 |
| 本地还有改动想补交 | `git add -A && git commit -m "..." && git push`（不要 force push） |
