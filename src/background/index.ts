chrome.runtime.onInstalled.addListener(async (opt) => {
  // Check if reason is install or update. Eg: opt.reason === 'install' // If extension is installed.
  // opt.reason === 'update' // If extension is updated.
  if (opt.reason === 'install') {
    await chrome.storage.local.clear()

    chrome.tabs.create({
      active: true,
      url: chrome.runtime.getURL('./src/setup/index.html?type=install'),
    })
  }

  // if (opt.reason === 'update') {
  //   chrome.tabs.create({
  //     active: true,
  //     url: chrome.runtime.getURL('./src/setup/index.html?type=update'),
  //   })
  // }
})

export {}
