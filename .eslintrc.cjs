/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution");

module.exports = {
  root: true,
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/eslint-config-typescript/recommended",
  ],
  parserOptions: {
    ecmaVersion: "latest",
  },
  globals: {
    "chrome": 'readonly'
  },
  rules: {
    "vue/multi-word-component-names": 0
  },
};
