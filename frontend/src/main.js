import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the updated router
import store from './store' // Make sure to import the store

createApp(App)
  .use(router)
  .use(store) // Use the Vuex store
  .mount('#app');
