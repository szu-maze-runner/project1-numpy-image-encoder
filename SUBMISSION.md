# 提交状态与最后一步（Project 1 · NumPy 图像编码器）

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
- **封面信息已全部填好**：专业「人工智能IEEE」、报告人「黄杨辰弘」、学号「2025681086」；
  课程名称、项目名称、学院、指导教师、实验/提交时间也已补齐。PDF 与 Word 两个版本都已填写，无需再改。
- **交付文件已按提交规范重命名**：`2025681086_黄杨辰弘_实验报告.pdf` / `.docx` / `.md`（学号_姓名_实验报告）。
- **仓库地址已填好**：README、两份报告、提交说明中均已写入，无需再复制粘贴。
- 326 MB 权重与参考输出按 GitHub 单文件上限排除，README 第 3 节写明获取方式与 SHA-256 校验。

## 二、你要交哪一个

| | 文件 | 说明 |
| --- | --- | --- |
| **推荐** | `report/2025681086_黄杨辰弘_实验报告.pdf` | 学院官方 LaTeX 模板，5 页，封面已填全，直接交 |
| 备选 | `report/2025681086_黄杨辰弘_实验报告.docx` | Word 版，5 页，封面已填全，方便再编辑 |

两份内容一致，任选其一即可，**不要都交**。若畅课只收 Word，交 docx；若收 PDF 或不限，交官方模板 PDF 更贴合老师预期。

## 三、你只剩一步

登录畅课 → 本小项目提交入口 → 上传报告 → 提交框粘贴
`https://github.com/szu-maze-runner/project1-numpy-image-encoder` → 刷新确认状态为「已提交」。

若平台强制要求另用官方 docx 模板，可打开 `report/2025681086_黄杨辰弘_实验报告.md`，
按「第 1~4 页」各节依次粘贴，粘贴后**预览确认总页数仍 ≤ 5 页**。

## 四、可编辑源文件（可选）

`report/official-template/main.tex` 是填好内容的 LaTeX 源（封面信息也已写入），`figs/` 是两张配图。
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
- [x] 封面个人信息与学号已填写，文件名已按「学号_姓名_实验报告」规范重命名
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
| 平台只收 Word | 交 `report/2025681086_黄杨辰弘_实验报告.docx` |
| 想改封面信息 | 改 `report/official-template/main.tex` 封面后重新编译两遍；Word 版可直接编辑 |
| 想再跑一次验证 | `python -m pip install -r requirements.txt` 后 `python check.py --stage all`（约 2 分钟） |
| 想改成私有并邀请助教 | 仓库 Settings → 改 visibility 为 Private → Collaborators 添加助教与老师账号 |
| 本地还有改动想补交 | `git add -A && git commit -m "..." && git push`（不要 force push） |
