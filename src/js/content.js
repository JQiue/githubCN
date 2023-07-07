const allData = [
  [`Recent Repositories`, `最近仓库`],
  [`Search or jump to…`, `搜索并跳转至...`],
  [`Issues`, `问题`],
  [`Pull`, `合并`],
  [`request`, `请求`],
  [`s`, ``],
  [`Marketplace`, `市场`],
  [`Explore`, `探索`],
  [`Following`, `关注者`],
  [`Find a repository…`, `查找仓库`],
  [`Latest changes`, `最新变化`],
  [`hours ago`, `小时前`],
  [`days ago`, `天前`],
  [`New`, `新建`],
  [`Explore repositories`, `探索存储库`],
  [`Explore more →`, `探索更多 →`],
  [`Set status`, `设置状态`],
  [`Your profile`, `个人信息`],
  [`Your repositories`, `个人仓库`],
  [`Your codespaces`, `你的 codespaces`],
  [`Your projects`, `你的项目`],
  [`Signed in as`, `登陆账户为`],
  [`Feature preview`, `功能预览`],
  [`Upgrade`, `升级`],
  [`Try Enterprise`, `尝试企业版`],
  [`Help`, `帮助`],
  [`Settings`, `设置`],
  [`Sign out`, `退出`],
  [`Overview`, `概述`],
  [`Repositories`, `仓库`],
  [`Projects`, `项目`],
  [`Packages`, `包`],
  [`Popular repositories`, `流行的仓库`],
  [`Edit profile`, `编辑个人信息`],
  [`followers`, ` 被关注`],
  [`following`, ` 关注`],
  [`Public`, `公开`],
  [`Customize your pins`, `定义你的置顶项目`],
  [`Contribution settings`, `贡献设置`],
  [`Pinned`, `置顶`],
  [`Learn how we count contributions`, `了解我们如何计算贡献`],
  [`Code review`, `代码评审`],
  [`Pull requests`, `合并请求`],
  [`Commits`, `提交`],
  [`Contribution activity`, `贡献活动`],
  [`Show more activity`, `显示更多活动`],
  [`Code`, `代码`],
  [`Go to file`, `转至文件`],
  [`Add file`, `添加文件`],
  [`About`, `关于`],
  [`Pin`, `置顶`],
  [`Pin this repository to your profile`, `置顶这个项目到你的个人信息`],
  [`New repository`, `新建仓库`],
  [`Import repository`, `导入仓库`],
  [`New organization`, `新建组织`],
  [`Create a new release`, `创建一个新的版本`],
  [`Publish your first package`, `发布你的第一个包`],
  [`Releases`, `发布`],
  [`Packages `, `包`],
  [`No packages published`, `没有发布任何软件包`],
  [`Languages`, `语言`],
  [`Show more`, `显示更多`],
  [`Recent activity`, `最新动态`],
  [
    `When you take actions across GitHub, we’ll provide links to that activity here.`,
    `当你在 GitHub 上采取行动时，我们会在这里提供该活动的链接。`,
  ],
  [`More`, `更多`],
  [`Subscribe to your news feed`, `订阅你的 feed`],
  [`Blog`, `博客`],
  [`Shop`, `商店`],
  [`Contact GitHub`, `联系 Github`],
  [`Pricing`, `定价`],
  [`Training`, `培训`],
  [`Status`, `状态`],
  [`Security`, `安全`],
  [`Terms`, `团队`],
  [`Privacy`, `隐私`],
  [`Docs`, `文档`],
  [`New project`, `新建项目`],
  [`Activity  overview`, `活动概览`],
  [`Projects`, `项目`],
  [`Security`, `安全`],
  [`Insights`, `统计`],
  [`Create new file`, `创建新的文件`],
  [`Upload files`, `上传文件`],
  [`Code`, `代码`],
  [`Local`, `本地`],
  [`Clone`, `克隆`],
  [`Open with GitHub Desktop`, `在 Github 桌面程序中打开`],
  [`Download ZIP`, `下载压缩包`],
  [`New codespace`, `新建 codespace`],
  [`Less`, `更少`],
  [`Select type`, `选择类型`],
  [`Type`, `类型`],
  [`Language`, `语言`],
  [`Sort`, `排序`],
  [`Private`, `私有`],
  [`Select language`, `选择语言`],
  [`Select order`, `选择顺序`],
  [`Last updated`, `最近更新`],
  [`Create a new repository`, `创建一个新的仓库`],
  [`Owner`, `拥有者`],
  [`Repository name`, `仓库名字`],
  [`Description`, `描述`],
  [`(optional)`, `(可选)`],
  [
    `Anyone on the internet can see this repository. You choose who can commit.`,
    `互联网上的任何人都可以看到这个存储库。你选择谁能够提交。`,
  ],
  [
    `You choose who can see and commit to this repository.`,
    `你可以选择谁可以看到和提交这个版本库。`,
  ],
  [
    `A repository contains all project files, including the revision history. Already have a project repository elsewhere?`,
    `一个仓库包含所有项目文件，包括修订历史。在其他地方已经有一个项目库了？`,
  ],
  [`Import a repository.`, `导入仓库`],
  [
    `Skip this step if you’re importing an existing repository.`,
    `如果你要导入一个已有的版本库，请跳过这一步。`,
  ],
  [
    `Choose which files not to track from a list of templates.`,
    `从一个模板列表中选择哪些文件不需要跟踪。`,
  ],
  [
    `This is where you can write a long description for your project.`,
    `在这里，你可以为你的项目写一个长的描述。`,
  ],
  [
    `A license tells others what they can and can't do with your code.`,
    `许可证告诉别人他们可以和不可以用你的代码做什么。`,
  ],
  [
    `You are creating a public repository in your personal account.`,
    `你正在你的个人账户中创建一个公共库。`,
  ],
  [`Initialize this repository with:`, `用以下方式初始化这个存储库：`],
  [`Create repository`, `创建仓库`],
  [
    `Great repository names are short and memorable. Need inspiration? How about`,
    `伟大的仓库名称是简短而令人难忘的。需要灵感吗？比如 `,
  ],
  [`Your personal account`, `你的个人账户`],
  [`Public profile`, `公开资料`],
  [`Name`, `名字`],
  [`Change username`, `修改用户名`],
  [`Account`, `账户`],
  [`Export account data`, `导出账户数据`],
  [`Appearance`, `外观`],
  [`Accessibility`, `无障碍设施`],
  [`Notifications`, `通知`],
  [`Access`, `访问`],
  [`Personal billing`, `个人帐单`],
  [`Emails`, `邮件`],
  [`Billing and plans`, `账单和计划`],
  [
    `This is a list of SSH keys associated with your account. Remove any keys that you do not recognize.`,
    `这是与你的账户相关的 SSH 密钥的列表，删除任何你不认识的密钥`,
  ],
  [`Organizations`, `组织`],
  [`You are not a member of any organizations.`, `你不是任何组织的成员  `],
  [`Archives`, `归档`],
  [`Security log`, `安全日志`],
  [`Sponsorship log`, `赞助日志`],
  [`No sponsorship activity in this time period`, `这段时间内没有赞助活动`],
  [`Sign in to GitHub`, `登录到 Github`],
  [`Username or email address`, `用户名或邮箱`],
  [`Password`, `密码`],
  [`Sign in`, `登录`],
  [`New to GitHub?`, `刚来 Github？`],
  [`Create an account`, `创建一个账户`],
  [`Forgot password?`, `忘记密码？`],
  [`Create an account`, ``],
  [
    `Label issues and pull requests for new contributors`,
    `为新的贡献者标记问题和合并请求`,
  ],
  [`Filters`, `过滤`],
  [`New Issue`, `新问题`],
  [`There aren’t any open issues.`, `没有任何公开的问题。`],
  [`Signing in…`, `登录中...`],
  [`Edit repository details`, `编辑仓库详情信息`],
  [`Website`, `网站`],
  [`Cancer`, `取消`],
  [`Save changes`, `保存修改`],
  [`Protect this branch`, `保护这个分支`],
  [`Get started with GitHub Actions`, `开始使用 Github Actions`],
  [
    `Build, test, and deploy your code. Make code reviews, branch management, and issue triaging work the way you want. Select a workflow to get started.`,
    `构建、测试和部署你的代码。使代码审查、分支管理和问题分流以你想要的方式进行。选择一个工作流程来开始。`,
  ],
  [`Browse all categories`, `浏览所有类型`],
  [`Automation`, `自动化`],
  [`Deployment`, `部署`],
  [`Continuous integration`, `持续集成`],
  [`Reporting`, `报告`],
  [`General`, `常规`],
  [`Public email`, `公开的邮箱`],
  [`Bio`, `个人简历`],
  [`URL`, `网站`],
  [`Twitter username`, `Twitter 用户名`],
  [`Company`, `公司`],
  [`Location`, `地址`],
  [`Contributions & Activity`, `贡献和活动`],
  [`Successor settings`, `继承人设置`],
  [`You have not designated a successor.`, `你还没有指定继承人`],
  [`Delete account`, `删除账户`],
  [
    `Once you delete your account, there is no going back. Please be certain.`,
    `一旦你删除了你的账户，就不能够找回了，请慎重`,
  ],
  [`Display current local time`, `显示当前的本地时间`],
  [`Keyboard shortcuts`, `快捷键`],
  [`Subscriptions`, `订阅`],
  [`Verified domains`, `验证的域名`],
  [`There are no verified domains.`, `没有经过验证的域名`],
  [`Password and authentication`, `密码和身份验证`],
  [`Change password`, `修改密码`],
  [`Old password`, `旧密码`],
  [`New password`, `新密码`],
  [`Confirm new password`, `确认新的密码`],
  [`Two-factor authentication`, `两步验证`],
  [`Confirm new password`, `确认新的密码`],
  [`Confirm access`, `确认访问`],
  [`Confirm`, `确认`],
  [`Who has access`, `谁有权限`],
  [`Code and automation`, `代码和自动化`],
  [`Default branch`, `默认分支`],
  [`Branch protection rules`, `分支保护规则`],
  [`Protected tags`, `保护标签`],
  [`Environments`, `环境变量`],
  [`Code security and analysis`, `代码安全性和分析`],
  [`Integrations`, `集成`],
  [`Email notifications`, `邮件通知`],
  [`Collaborators`, `合作者`],
  [`Contributors`, `贡献者`],
  [`Community Standards`, `社区标准`],
  [`Traffic`, `流量`],
  [`Code frequency`, `代码频率`],
  [`Dependency graph`, `依赖图`],
  [`Contributors`, `贡献者`],
  [`You can`, `你可以`],
  [`@mention`, `@`],
  [
    `other users and organizations to link to them.`,
    `其他用户和组织来链接它们`,
  ],
  [`Save`, `保存`],
  [`Cancel`, `取消`],
  [`Welcome to the all-new projects`, `欢迎来到全新的项目`],
  [`No open projects`, `没有开放的项目`],
  [`Add a bio`, `添加个人简介`],
  [`Loading more...`, `正在加载中`],
  [
    `Your popular repositories will now be shown instead of your pins.`,
    `你的热门仓库现在将显示，而不是你的置顶`,
  ],
  [`Unpin`, `不置顶`],
  [`Your pins have been updated.`, `你的置顶已经更新了`],
  [`Advanced search`, `高级搜索`],
  [`Branches`, `分支`],
  [`Social Preview`, `社交预览`],
  [
    `Upload an image to customize your repository’s social media preview.`,
    `上传图片来定制你仓库的社交媒体预览`,
  ],
  [`Pull Requests`, `合并请求`],
  [`Danger Zone`, `危险区`],
  [`Change repository visibility`, `修改仓库的可见性`],
  [`Transfer ownership`, `转让所有权`],
  [`This repository is currently public.`, `这个仓库当前是公开的`],
  [`Archive this repository`, `归档这个仓库`],
  [
    `Mark this repository as archived and read-only.`,
    `将此版本库标记为归档和只读`,
  ],
  [`Delete this repository`, `删除这个仓库`],
  [
    `Once you delete a repository, there is no going back. Please be certain.`,
    `一旦你删除了这个仓库，就不能够撤回了，请确认`,
  ],
  [`Are you absolutely sure?`, `你真的确定吗？`],
  [`Change visibility`, `修改可见性`],
  [`Change to private`, `修改为私有`],
  [`Transfer`, `转移`],
  [`Edit status`, `编辑状态`],
  [`Busy`, `忙`],
  [`Clear status`, `清除状态`],
  [`Never`, `从不`],
  [`Your main branch isn't protected`, `你的 main 分支不是受保护的`],
  [
    `Protect this branch from force pushing or deletion, or require status checks before merging.`,
    `保护这个分支不被强行推送或删减，或要求在合并前进行状态检查 `,
  ],
  [`Learn more`, `学习更多`],
  [`Branch protection rule`, `分支保护规则`],
  [`Protect your most important branches`, `保护你最重要的分支`],
  [`Achievements`, `成就`],
  [`Send feedback`, `发送反馈`],
  [`Choose a license`, `选择许可证`],
  [`Learn more.`, `学习更多`],
  [`Import your project to GitHub`, `导入你得项目到 Github`],
  [`Inbox`, `收件箱`],
  [`Prev`, `上页`],
  [`Next`, `下页`],
  [`Saved`, `保存`],
  [`Done`, `完成`],
  [`Manage notifications`, `管理通知`],
  [`See more`, `查看更多`],
  [`Include in the home page`, `显示在页面上`],
  [`Discussions`, `讨论`],
  [`Users`, `用户`],
  [`This repository is currently private.`, `这个仓库当前是私有的`],
  [`Lists`, `列表`],
  [`Create list`, `创建列表`],
  [`Pushes`, `推送`],
  [
    `Limit how many branches and tags can be updated in a single push`,
    `限制一次推送中可以更新多少个分支和标签`,
  ],
  [`I want to make this repository private`, `我想要让这个仓库变为私有`],
  [`I have read and understand these effects`, `我已经阅读并理解了这些影响`],
  [`New issue`, `新建问题`],
  [`Labels`, `标签`],
  [`New milestone`, `新建里程碑`],
  [`Milestones`, `里程碑`],
  [`You haven’t created any Milestones.`, `你还没有创建任何里程碑。`],
  [`Edit`, `编辑`],
  [`Delete`, `删除`],
  [`Close`, `关闭`],
  [`Success`, `完成`],
  [``, ``],
  [``, ``],
  [``, ``],
  [``, ``],
  [``, ``],
  [``, ``],
  [``, ``],
  [``, ``],
];

const MutationObserverConfig = {
  childList: true,
  subtree: true,
  attributeFilter: ["data-label"],
  characterData: true,
};

const observer = new MutationObserver(function (mutations) {
  const treeWalker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_ALL,
    {
      acceptNode: function (node) {
        if (
          node.nodeType === 3 ||
          (node.hasAttribute &&
            (node.hasAttribute("data-label") ||
              node.hasAttribute("placeholder") ||
              node.hasAttribute("value")))
        ) {
          return NodeFilter.FILTER_ACCEPT;
        } else {
          return NodeFilter.FILTER_SKIP;
        }
      },
    },
    false
  );
  let dataMap = new Map();
  allData.forEach(([key, val]) => {
    if (key && !dataMap.has(key)) {
      dataMap.set(key, val);
    }
  });
  let currentNode = treeWalker.currentNode;
  while (currentNode) {
    if (currentNode.nodeType === 3) {
      let key1 = currentNode.textContent
        .replace(/^\s*|\s*$/g, "")
        .replace(/\s+/g, " ");
      if (dataMap.has(key1)) currentNode.textContent = dataMap.get(key1);
    } else {
      let key2 = currentNode.getAttribute("data-label");
      if (key2 && dataMap.has(key2))
        currentNode.setAttribute("data-label", dataMap.get(key2));
      let key3 = currentNode.getAttribute("placeholder") || "";
      if ((key3 = key3.trim())) {
        if (dataMap.has(key3))
          currentNode.setAttribute("placeholder", dataMap.get(key3));
      }
      let key4 = currentNode.getAttribute("value");
      if (currentNode.tagName == "INPUT" && dataMap.has(key4)) {
        currentNode.setAttribute("value", dataMap.get(key4));
        let key5 = currentNode.getAttribute("data-signin-label");
        let key6 = currentNode.getAttribute("data-disable-with");
        currentNode.setAttribute("data-signin-label", dataMap.get(key5));
        currentNode.setAttribute("data-disable-with", dataMap.get(key6));
      }
    }
    currentNode = treeWalker.nextNode();
  }
});

observer.observe(document.body, MutationObserverConfig);
