import packageJson from "../package.json";
import type { ManifestType } from "./manifest-type";

const manifest: ManifestType = {
  manifest_version: 3,
  name: "GithubCN",
  version: packageJson.version,
  description: packageJson.description,
  // options_page: "src/options/index.html",
  // devtools_page: "src/devtools/index.html",
  background: { service_worker: "src/background/index.js" },
  // action: {
  //   default_popup: "src/popup/index.html",
  //   default_icon: "icon-34.png",
  // },
  // chrome_url_overrides: {
  //   newtab: "src/newtab/index.html",
  // },
  icons: {
    "16": "icon-16.png",
    "34": "icon-34.png",
    "48": "icon-48.png",
  },
  content_scripts: [
    {
      js: ["src/content/index.js"],
      matches: ["https://github.com/*"],
      run_at: "document_end",
      all_frames: true,
    },
  ],
  web_accessible_resources: [
    {
      resources: ["icon-48.png", "icon-34.png", "icon-16.png"],
      matches: [],
    },
  ],
};

export default manifest;
