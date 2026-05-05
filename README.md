# GithubCN

> 由于个人精力不足，不再为此项目添加词条内容，如有余力，可 fork 本项目进行词条补充

Github 浏览器中文汉化插件

## 安装 && 使用

支持的浏览器|使用方式
---|---
Edge|[Edge 应用商店](<https://microsoftedge.microsoft.com/addons/detail/githubcn/onlodfoebaobhmlhgcbddjngjbkdbfaj>)
Google Chrome|下载源代码拖放至扩展页

## 如何补充翻译词条？

所有的翻译内容都在在`src/js/content.js`中

```js
const allData = [
  [`English`, `英文`],
]
```

## v1.5.0 更新

由社区贡献，系统性补充了约 400+ 条翻译词条，主要覆盖以下功能模块：

- **导航栏** - 顶部导航、登录注册、底部链接
- **个人资料页** - Profile、关注者、置顶、成就
- **仓库详情页** - 文件浏览、克隆、分支、标签、话题
- **新建仓库** - 完整的新建仓库流程翻译
- **Issue 页面** - 筛选、排序、指派、标签、里程碑
- **Pull Request 页面** - 审查、合并、差异对比、CI 检查
- **仓库设置** - 危险区域、可见性、归档、删除
- **仓库 Insights** - Pulse、贡献者、流量、依赖图
- **用户设置** - 密码、安全、通知、SSH 密钥
- **GitHub Actions** - 工作流、运行、检查、制品
- **安全页面** - 代码扫描、Dependabot、密钥扫描
- **Wiki** - 页面创建、编辑、历史
- **通知** - 收件箱、已读/未读、参与
- **搜索** - 高级搜索、筛选、排序
- **Gist** - 创建、克隆、嵌入
- **GitHub Copilot** - Copilot Chat、商业版/个人版
- **Codespaces** - 创建、打开方式
- **GitHub Pages** - 构建部署、自定义域名
- **Trending** - 热门仓库、热门开发者
- **通用** - 按钮操作、时间表示、错误页面

同时修复了以下翻译错误：
- `Cancer` -> `Cancel`（原文笔误）
- `Terms` 翻译为"团队" -> 修正为"条款"
- 统一了"仓库"/"存储库"等术语翻译
