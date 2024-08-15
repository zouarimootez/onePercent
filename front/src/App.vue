<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import { isAuthenticated } from './auth';

export default {
  name: 'App',
  beforeMount() {
    if (isAuthenticated()) {
      this.$router.replace('/hello');
    } else {
      this.$router.replace('/login');
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
