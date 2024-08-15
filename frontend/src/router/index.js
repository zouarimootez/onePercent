import { createRouter, createWebHistory } from 'vue-router';
import GameBoard from '@/components/GameBoard.vue'; // Adjust path if necessary

const routes = [
  {
    path: '/',
    name: 'GameBoard',
    component: GameBoard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
