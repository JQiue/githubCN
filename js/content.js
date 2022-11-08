const allData = [
  [
    `
      Recent Repositories
      `,
    `最近仓库`,
  ],
  [`Search or jump to…`, `搜索或跳转至...`],
  [`Issues`, `议题`],
  [`\n      Pull`, `合并`],
  [` request`, `请求`],
  [`s\n`, ``],
  [`Marketplace`, `市场`],
  [`Explore`, `探索`],
  [`Following`, `关注者`],
  [`Find a repository…`, `查找仓库`],
  [`Latest changes`, `最新变动`],
  [`hours ago`, `小时前`],
  [`days ago`, `天前`],
  [` New\n`, `新建`],
  [`Explore repositories`, `探索存储库`],
  [`\n      Explore more →\n`, `探索更多 →`],
  [`Set status`, `设置状态`],
  [`Your profile`, `个人信息`],
  [`Your repositories`, `个人仓库`],
  [`Your codespaces`, `你的代码空间`],
  [`Your projects`, `你的项目`],
  [`Signed in as `, `登陆账户为`],
  [`\n    Feature preview\n  `, `功能预览`],
  [`Upgrade`, `升级`],
  [`Try Enterprise`, `尝试企业版`],
  [`Help`, `帮助`],
  [`Settings`, `设置`],
  [`\n    Sign out\n  `, `退出`],
  [`\n    Overview\n`, `概述`],
  [`\n    Repositories\n    `, `仓库`],
  [`\n    Projects\n    `, `项目`],
  [`\n      Packages\n      `, `包`],
  [`\n      Popular repositories\n    `, `流行的仓库`],
  [`Edit profile`, `编辑个人信息`],
  [`\n          followers\n`, ` 被关注`],
  [`\n          following\n`, ` 关注`],
  [`Public`, `公开`],
  [`Customize your pins`, `定义你的置顶项目`],
  [`\n    Contribution settings\n    `, `贡献设置`],
  [`\n      Pinned\n    `, `置顶`],
  [`\n              Learn how we count contributions`, `了解我们如何计算贡献`],
  [`Code review`, `代码评审`],
  [`Pull requests`, `合并请求`],
  [`Commits`, `提交`],
  [`\n    Contribution activity\n  `, `贡献活动`],
  [`Show more activity`, `显示更多活动`],
  [`Code`, `代码`],
  [`\n  Go to file\n`, `转至文件`],
  [`\n        Add file\n        `, `添加文件`],
  [`About`, `关于`],
  [`Pin\n`, `置顶`],
  [`Pin this repository to your profile`, `置顶这个项目到你的个人信息`],
  [`\n  New repository\n`, `新建仓库`],
  [`\n    Import repository\n  `, `导入仓库`],
  [`\n    New organization\n  `, `新建组织`],
  [`Create a new release`, `创建一个新的版本`],
  [`Publish your first package`, `发布你的第一个包`],
  [`\n    Releases\n`, `发布`],
  [`\n    Packages `, `包`],
  [`\n        No packages published `, `没有发布任何软件包`],
  [`Languages`, `语言`],
  [``, ``],
  [``, ``],
  [``, ``],
  [``, ``],
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
              node.hasAttribute("placeholder")))
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
      let key1 = currentNode.textContent;
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
    }

    currentNode = treeWalker.nextNode();
  }
});

observer.observe(document.body, MutationObserverConfig);

console.log("已经汉化");
console.log(`\n\n`);
