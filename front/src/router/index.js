// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/LoginPage.vue';
import HelloPage from '../components/HelloPage.vue';

const routes = [
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/hello', name: 'HelloPage', component: HelloPage },
  { path: '/', redirect: '/login' }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
