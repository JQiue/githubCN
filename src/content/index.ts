import { entry as allData } from "./data.json";

function debounce(func, delay) {
  let timeout;
  return function (args) {
    if (timeout) clearTimeout(timeout);
    const flag = !timeout;
    timeout = setTimeout(() => (timeout = null), delay);
    if (flag) func.apply(this, args);
  };
}

const specifyChange = () => {
  const inputQueryChildNodes =
    document.querySelector("#qb-input-query")?.childNodes;

  if (inputQueryChildNodes) {
    console.log("has");
    inputQueryChildNodes[0].textContent = "按下";
    inputQueryChildNodes[2].textContent = "搜索";
  }
  console.log("specify");
  
};

const debounceHandle = debounce(specifyChange, 100);

const MutationObserverConfig = {
  childList: true,
  subtree: true,
  attributeFilter: ["data-label"],
  characterData: true,
};

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const observer = new MutationObserver(function (_mutations) {
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
  const dataMap = new Map();
  allData.forEach(([key, val]) => {
    if (key && !dataMap.has(key)) {
      dataMap.set(key, val);
    }
  });
  let currentNode = treeWalker.currentNode;
  while (currentNode) {
    if (currentNode.nodeType === 3) {
      const key1 = currentNode.textContent
        .replace(/^\s*|\s*$/g, "")
        .replace(/\s+/g, " ");
      if (dataMap.has(key1)) currentNode.textContent = dataMap.get(key1);
    } else {
      const key2 = currentNode.getAttribute("data-label");
      if (key2 && dataMap.has(key2))
        currentNode.setAttribute("data-label", dataMap.get(key2));
      let key3 = currentNode.getAttribute("placeholder") || "";
      if ((key3 = key3.trim())) {
        if (dataMap.has(key3))
          currentNode.setAttribute("placeholder", dataMap.get(key3));
      }
      const key4 = currentNode.getAttribute("value");
      if (currentNode.tagName == "INPUT" && dataMap.has(key4)) {
        currentNode.setAttribute("value", dataMap.get(key4));
        const key5 = currentNode.getAttribute("data-signin-label");
        const key6 = currentNode.getAttribute("data-disable-with");
        currentNode.setAttribute("data-signin-label", dataMap.get(key5));
        currentNode.setAttribute("data-disable-with", dataMap.get(key6));
      }
    }
    currentNode = treeWalker.nextNode();
  }
  debounceHandle(null);
});

observer.observe(document.body, MutationObserverConfig);

console.log("已汉化");
