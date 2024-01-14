import { defineManifest } from '@crxjs/vite-plugin'
import packageJson from './package.json'

const { version, name, description, displayName } = packageJson
// Convert from Semver (example: 0.1.0-beta6)
const [major, minor] = version
  // can only contain digits, dots, or dash
  .replace(/[^\d.-]+/g, '')
  // split into version parts
  .split(/[.-]/)

export default defineManifest(async (env) => ({
  name: env.mode === 'staging' ? `[INTERNAL] ${name}` : displayName || name,
  description,
  // up to four numbers separated by dots
  version: `${major}.${minor}`,
  // semver is OK in "version_name"
  manifest_version: 3,
  // key: 'ekgmcbpgglflmgcfajnglpbcbdccnnje',
  homepage_url: 'https://github.com/JQiue/githubCN',
  icons: {
    '16': 'src/assets/images/icon-16.png',
    '48': 'src/assets/images/icon-48.png',
    '128': 'src/assets/images/icon-128.png',
  },
  // action: {
  //   default_popup: 'src/popup/index.html',
  // },
  background: {
    service_worker: 'src/background/index.ts',
  },
  content_scripts: [
    {
      matches: ['https://github.com/*'],
      js: ['src/content-script/index.ts'],
      run_at: 'document_end',
      all_frames: true,
    },
  ],
  // options_page: 'src/options/index.html',
  permissions: ['storage'],
  // web_accessible_resources: [],
}))
