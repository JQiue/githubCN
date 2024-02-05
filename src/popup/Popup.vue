<script setup lang="ts">
import { ref } from "vue";
const msg = ref("hello world");
</script>
<template>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="../assets/vue.svg"
      width="125"
      height="125"
    />

    <div class="wrapper">
      <div class="greetings">
        <h1 class="green">{{ msg }}</h1>
        <h3>
          You’ve successfully created a project with
          <a target="_blank" href="https://vitejs.dev/">Vite</a> +
          <a target="_blank" href="https://vuejs.org/">Vue 3</a>.
        </h3>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
