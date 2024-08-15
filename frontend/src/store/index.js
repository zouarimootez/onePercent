import Vuex from 'vuex';
import axios from 'axios';

export default new Vuex.Store({
  state: {
    games: [],
    currentGame: null,
    token: localStorage.getItem('access_token') || '',  // Retrieve token from local storage
  },
  mutations: {
    SET_GAMES(state, games) {
      state.games = games;
    },
    SET_CURRENT_GAME(state, game) {
      state.currentGame = game;
    },
    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem('access_token', token);  // Store token in local storage
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post('http://localhost:8000/api/token/', credentials);
        const token = response.data.access;
        commit('SET_TOKEN', token);
        // Optionally redirect to a protected page
      } catch (error) {
        console.error('Login error:', error);
      }
    },

    async fetchGames({ commit, state }) {
      try {
        const response = await axios.get('http://localhost:8000/api/games/', {
          headers: {
            'Authorization': `Bearer ${state.token}`,  // Include the Bearer token
          },
        });
        commit('SET_GAMES', response.data);
      } catch (error) {
        console.error('API error:', error);
      }
    },
    async createGame({ commit, state }, gameData) {
      try {
        const response = await axios.post('http://localhost:8000/api/games/', gameData, {
          headers: {
            'Authorization': `Bearer ${state.token}`,  // Include the Bearer token
          },
        });
        commit('SET_CURRENT_GAME', response.data);
      } catch (error) {
        console.error('API error:', error);
      }
    },
  },
});
