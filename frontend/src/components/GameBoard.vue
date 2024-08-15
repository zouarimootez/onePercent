<template>
    <div>
        <h1>Ludo Game</h1>
        <div v-if="currentGame">
            <h2>Current Turn: {{ currentGame.current_turn }}</h2>
            <button @click="rollDice">Roll Dice</button>
            <p>Dice Value: {{ diceValue }}</p>
        </div>
        <div v-else>
            <p>Loading game...</p>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
    computed: {
        ...mapState(['currentGame']),
    },
    data() {
        return {
            diceValue: null,
        };
    },
    created() {
        if (!this.currentGame) {
            console.log("Fetcheeee");
            this.$store.dispatch('fetchGames'); // Fetch games if not already fetched
        }
    },
    methods: {
        rollDice() {
            this.diceValue = Math.floor(Math.random() * 6) + 1;
            // Additional logic to update the game state
        },
    },
};
</script>
