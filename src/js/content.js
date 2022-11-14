const allData = [
  [`Recent Repositories`, `最近仓库`],
  [`Search or jump to…`, `搜索或跳转至...`],
  [`Issues`, `问题`],
  [`Pull`, `合并`],
  [`request`, `请求`],
  [`s`, ``],
  [`Marketplace`, `市场`],
  [`Explore`, `探索`],
  [`Following`, `关注者`],
  [`Find a repository…`, `查找仓库`],
  [`Latest changes`, `最新变动`],
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
  [`No packages published `, `没有发布任何软件包`],
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
];

let MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
let MutationObserverConfig = {
  childList: true,
  subtree: true,
  attributeFilter: ["data-label"],
  characterData: true,
};

let observer = new MutationObserver(function (mutations) {
  let treeWalker = document.createTreeWalker(
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

console.log("已经汉化");
console.log(`\n\n`);
