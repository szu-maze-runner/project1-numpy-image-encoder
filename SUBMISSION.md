# 提交操作指南（Project 1 · NumPy 图像编码器）

> 按截图要求，需要交 **两样东西**：① GitHub 仓库地址（写进实验报告 + 畅课提交框，
> 且向助教和老师开放权限）；② 实验报告（正文 ≤ 5 页，模板在畅课平台）。
> 本仓库已完成代码、README、依赖清单、结果证据和 4 页报告，你只需完成下面的「推送 + 填写 + 上传」。

## 一、交付物清单（已备好，在 `D:\桌面\project1-numpy-student`）

| 文件 / 目录 | 作用 | 交到哪里 |
| --- | --- | --- |
| `image_encoder.py` | 补全 TODO-01~06 的核心实现 | GitHub 仓库 |
| `README.md` | 代码功能、结构、依赖、数据获取、运行步骤、实测结果 | GitHub 仓库（必需） |
| `requirements.txt`、`config.json` | 依赖清单、模型结构参数 | GitHub 仓库 |
| `helpers.py` 等课程提供的脚本 | 可运行源码 | GitHub 仓库 |
| `assets/images/*.jpg`、`images.json`、两个 `manifest.json` | 10 张小图、ID、SHA-256 指纹 | GitHub 仓库 |
| `.gitignore` | 排除 326 MB 权重与参考输出 | GitHub 仓库 |
| `results/` | 校验日志、误差表、证据图、输出特征、相似度矩阵 | GitHub 仓库（结果证据） |
| `report/实验报告.docx` | 4 页实验报告，可直接上传 | 畅课平台 |
| `report/实验报告.md` | 同样内容的纯文本版，便于粘贴进畅课模板 | 备用 |
| `docs/COURSE-README.md` | 课程原始 README 备份 | GitHub 仓库 |
| `SUBMISSION.md` | 本指南 | 自留，可一并提交 |

**不随仓库提交**：`weights/image_encoder.npz`（311 MiB）、`assets/reference_outputs.npz`（7.3 MiB）。
前者超过 GitHub 单文件 100 MB 上限，README 第 3 节写明了从课程附件获取的方法与 SHA-256 校验命令，
满足「必要数据或获取方法」的要求；助教按说明复制两个文件即可完整复现。

## 二、GitHub 提交（约 5 分钟，需你本人登录账号）

本机已安装 Git 2.55，且**本仓库已初始化为 `main` 分支并保留了 3 条真实提交**
（导入课程文件 → 补全 6 组 TODO → 添加 README/证据/报告）。先确认：

```bash
cd "D:\桌面\project1-numpy-student"
git log --oneline          # 应看到 3 条提交
git status                  # 应显示 working tree clean
```

### 步骤 1：在 GitHub 网页新建空仓库
1. 浏览器登录你自己的 GitHub → 右上角 `+` → `New repository`。
2. 仓库名建议 `project1-numpy-image-encoder`，选择 **Private**（私有）。
3. **不要**勾选 `Add a README file` / `.gitignore` / license，保持空仓库，避免推送冲突。

### 步骤 2：向助教和老师开放权限（截图明确要求）
`Settings` → `Collaborators`（左侧）→ `Add people` → 输入助教和老师的 GitHub 用户名或邮箱 →
`Add ... to this repository`，对方接受邀请后即可 clone 查看提交记录。
也可把仓库改为 Public（简单但代码公开）。**请务必确认两人都能打开仓库链接**，
可在无痕/未登录浏览器里测试，或请助教确认。

### 步骤 3：关联远程仓库并推送
把 `<用户名>`、`<仓库名>` 换成你自己的：

```bash
cd "D:\桌面\project1-numpy-student"
git remote add origin https://github.com/<用户名>/<仓库名>.git
git branch -M main
git push -u origin main
```

首次推送若弹出登录，按提示用浏览器授权；若要求密码，使用 GitHub
`Settings → Developer settings → Personal access tokens` 生成的 token 代替密码。
（不要 force push、不要 squash、不要删掉 `.git` 重新一次性提交——评分要求**保留真实提交记录**。）

### 步骤 4：网页验收
- 首页能正确渲染 `README.md`，文件树里有 `image_encoder.py`、`requirements.txt`、`results/`、`report/`；
- `Commits` 页能看到 3 条提交及时间，点开能看到代码差异；
- 仓库体积只有几 MB（说明大文件已被 `.gitignore` 正确排除）；
- 确认助教/老师账号能访问。

复制地址栏链接，例如 `https://github.com/<用户名>/project1-numpy-image-encoder`。

## 三、填写并提交实验报告到畅课平台

1. 在畅课平台下载**实验报告模板**，用 Word / WPS 打开。
2. 两种用法：
   - 平台接受 docx → 直接上传 `report/实验报告.docx`（已按 4 页排版，含误差表与证据图）；
   - 必须用官方模板 → 打开 `report/实验报告.md`，把「第 1~4 页」各节内容依次粘贴进模板对应栏目
     （任务与方法 / 可复现性 / 结果与证据 / 分析与反思 / 本人贡献）。
3. **填写占位内容**：姓名、学号，以及第 1 页和第 4 页的 `GitHub 地址 ____`、`____（提交前填写）`
   —— 粘贴步骤 4 复制的链接。
4. **页数红线**：正文控制在 5 页以内（当前 4 页），超过 5 页将得 60 分以下。
   粘贴到模板后请预览一次，若模板自带封面/目录，注意别让正文被撑到 6 页；
   必要时删掉次要文字，优先保留误差表、证据图和分析反思。
5. 在畅课提交框里同时**粘贴 GitHub 地址**（截图要求「可放在实验报告中」），
   然后提交。提交后刷新页面确认状态为「已提交」。

## 四、提交前自检清单

- [ ] `image_encoder.py` 6 组 TODO 全部实现，无 `NotImplementedError`
- [ ] 本机 `python check.py --stage all` 8 个阶段全 PASS（实测结果见 `results/check_log.txt`）
- [ ] README.md 说明了代码功能、结构、依赖、数据获取、运行步骤
- [ ] GitHub 仓库已向助教和老师开放权限，且能看到多条真实 commit
- [ ] 报告 ≤ 5 页，写明任务、方法、本人贡献、结果证据、分析反思，并填入 GitHub 地址
- [ ] 没有把 326 MB 权重或参考输出误传（或已用 Git LFS）
- [ ] 没有在最后一刻提交；不接受无理由迟交

## 五、规则提醒（来自截图）

- 成绩构成：**代码 30 分 + 报告 70 分**；本小项目占最终成绩的 **10%**。
- 代码评分看功能与完成度、逻辑与算法、规范与鲁棒性；报告评分看任务与方法、可复现性、
  结果与证据、分析与反思。
- 有任何问题及时请教助教或老师；**迟交 N 天，最终得分 = 批改得分 × (1 − 0.1·N)**，
  且不接受无理由迟交。

## 六、常见问题

| 现象 | 处理 |
| --- | --- |
| `git push` 提示远程有内容 | 先 `git pull --rebase origin main` 再 `git push`；不要用 `--force` |
| 忘记勾选权限 | 补做步骤 2，并请助教确认能打开 |
| 助教说缺权重文件 | 请其按 README 第 3 节从课程附件复制两个 `.npz`，或你改用 Git LFS：`git lfs install && git lfs track "weights/*.npz"` 后重新提交 |
| 平台只收 PDF | 用 Word/WPS 打开 `实验报告.docx` → 另存为 PDF，检查仍 ≤ 5 页 |
| 想再跑一次验证 | `python -m pip install -r requirements.txt` 后 `python check.py --stage all`（约 2 分钟） |
