import { defineConfig } from "vite";
import { resolve } from "path";
import vue from "@vitejs/plugin-vue";
import makeManifest from "./scripts/make-manifest";

const src = resolve(__dirname, "src");
const assetsDir = resolve(src, "assets");
const outDir = resolve(__dirname, "dist");
const publicDir = resolve(__dirname, "public");

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      "@src": src,
      "@assets": assetsDir,
    },
  },
  plugins: [vue(), makeManifest()],
  publicDir,
  css: {
    // Global SCSS Imports 使用 scss.additionalData 来编译所有应用 scss 变量的组件
    preprocessorOptions: {
      scss: {
        additionalData: '@use "@src/styles/variable.scss" as *;',
      },
    },
  },
  build: {
    outDir,
    rollupOptions: {
      input: {
        content: resolve(src, "content", "index.ts"),
        background: resolve(src, "background", "index.ts"),
        popup: resolve(src, "popup", "index.html"),
        newtab: resolve(src, "newtab", "index.html"),
        devtools: resolve(src, "devtools", "index.html"),
        options: resolve(src, "options", "index.html"),
      },
      output: {
        entryFileNames: (chunk) => `src/${chunk.name}/index.js`,
      },
    },
  },
});
