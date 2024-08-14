from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_as_player1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_as_player2')
    current_turn = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_turn_game')
    board_state = models.JSONField(default=dict)  # Store game state
    status = models.CharField(max_length=10, default='waiting')  # waiting, playing, finished

class DiceRoll(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    roll_value = models.IntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE)
