# 提交状态与最后两步（Project 1 · NumPy 图像编码器）

## 一、已完成（无需你操作）

- **公开仓库已创建并推送**：https://github.com/szu-maze-runner/project1-numpy-image-encoder
  （Public，助教与老师可直接访问；`main` 分支，保留多条真实提交，未 squash / force push）。
- 仓库内含：补全的 `image_encoder.py`、中文 `README.md`、`requirements.txt`、`config.json`、
  课程提供的可运行脚本、10 张小图与指纹清单、`results/`（校验日志、误差表、证据图、输出特征、
  相似度矩阵）、`report/`（最终报告 docx + md）、`.gitignore`。
- **报告已按课程实验报告版式排好**：宋体 22pt 居中大标题 + 14pt 封面信息表 +
  「一、二、三…」章标题 / 12pt 小节 / 10.5pt 两端对齐正文、A4 页边距，
  共 **5 页（封面 1 页 + 正文 4 页）**，符合「正文 ≤ 5 页」要求。
- **仓库地址已填好**：`README.md`、`report/实验报告.docx`、`report/实验报告.md` 中均已写入，
  无需再复制粘贴。
- 326 MB 权重与参考输出按 GitHub 单文件上限排除，README 第 3 节写明获取方式与 SHA-256 校验。

## 二、你只剩两步

1. **填封面信息**：用 Word / WPS 打开 `report/实验报告.docx`，把封面表格里的
   「课程名称、学院、专业、指导教师、报告人、学号」六处 `（填写）` 换成你的真实信息，保存。
   （项目名称、实验/提交时间、GitHub 地址已填好，不用改。）
2. **交到畅课平台**：登录畅课 → 找到本小项目提交入口 → 上传这份 `实验报告.docx`，
   并在提交框里粘贴仓库地址 `https://github.com/szu-maze-runner/project1-numpy-image-encoder`，
   提交后刷新确认状态为「已提交」。

若平台强制要求用官方模板，可打开 `report/实验报告.md`，按「第 1~4 页」各节内容依次粘贴，
粘贴后**预览确认总页数仍 ≤ 5 页**。

## 三、验收清单

- [x] `image_encoder.py` 6 组 TODO 全部实现，无 `NotImplementedError`
- [x] `python check.py --stage all` 8 个阶段全 PASS（原始日志 `results/check_log.txt`）
- [x] README.md 说明代码功能、结构、依赖、数据获取与运行步骤
- [x] GitHub 仓库为 Public，能看到多条真实 commit，仓库体积只有几 MB
- [x] 报告 ≤ 5 页，含任务与方法、可复现性、结果证据、分析反思、本人贡献，并已填入仓库地址
- [ ] 封面个人信息已填写
- [ ] 畅课平台已上传报告并粘贴仓库地址
- [ ] 没有在最后一刻提交；不接受无理由迟交

## 四、规则提醒（来自截图）

- 成绩构成：**代码 30 分 + 报告 70 分**；本小项目占最终成绩的 **10%**。
- 报告**超过 5 页将得 60 分以下**；当前 5 页，若粘贴到别的模板请重新预览页数。
- 迟交 N 天，最终得分 = 批改得分 × (1 − 0.1·N)；有疑问及时请教助教或老师。

## 五、常见问题

| 现象 | 处理 |
| --- | --- |
| 助教说缺权重文件 | 按 README 第 3 节从课程附件复制 `weights/image_encoder.npz` 与 `assets/reference_outputs.npz` 到对应目录（GitHub 单文件限 100 MB） |
| 平台只收 PDF | Word/WPS 打开 `实验报告.docx` → 另存为 PDF，检查仍 ≤ 5 页 |
| 想再跑一次验证 | `python -m pip install -r requirements.txt` 后 `python check.py --stage all`（约 2 分钟） |
| 想改成私有并邀请助教 | 仓库 Settings → 改 visibility 为 Private → Collaborators 添加助教与老师账号 |
| 本地还有改动想补交 | `git add -A && git commit -m "..." && git push`（不要 force push） |
