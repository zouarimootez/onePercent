// store/index.js
import Vuex from 'vuex';
import axios from 'axios';
export default new Vuex.Store({
    state: {
      games: [],
      currentGame: null,
    },
    mutations: {
      SET_GAMES(state, games) {
        state.games = games;
      },
      SET_CURRENT_GAME(state, game) {
        state.currentGame = game;
      },
    },
    actions: {
      async fetchGames({ commit }) {
        console.log('fetchGames action called'); // Debugging line
        try {
          const response = await axios.get('http://worldtimeapi.org/api/timezone/Europe/London');
          commit('SET_GAMES', response.data);
          console.log('API response:', response.data); // Debugging line
        } catch (error) {
          console.error('API error:', error); // Debugging line
        }
      },
      async createGame({ commit }, gameData) {
        console.log('createGame action called'); // Debugging line
        try {
          const response = await axios.post('http://worldtimeapi.org/api/timezone/Europe/London', gameData);
          commit('SET_CURRENT_GAME', response.data);
          console.log('Created game:', response.data); // Debugging line
        } catch (error) {
          console.error('API error:', error); // Debugging line
        }
      },
    },
  });
  