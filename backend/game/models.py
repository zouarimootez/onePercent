from django.db import models
from django.contrib.auth.models import AbstractUser

class OPUser(AbstractUser):
    # Adding additional fields
    opusername = models.CharField(max_length=255, blank=True, null=True)
    oppassword = models.CharField(max_length=255, blank=True, null=True)
    flous = models.IntegerField(default=0)  # Ensure default value is provided
    diamond = models.IntegerField(default=0)  # Ensure default value is provided


    # Optional: Override save method to ensure `opusername` and `oppassword` reflect the User's username
    def save(self, *args, **kwargs):
        if not self.opusername:
            self.opusername = self.username
        if not self.oppassword:
            self.oppassword = self.password
        super().save(*args, **kwargs)
    pass
"""class Game(models.Model):
    player1 = models.ForeignKey(OPUser, on_delete=models.CASCADE, related_name='games_as_player1')
    player2 = models.ForeignKey(OPUser, on_delete=models.CASCADE, related_name='games_as_player2')
    current_turn = models.ForeignKey(OPUser, on_delete=models.CASCADE, related_name='current_turn_game')
    board_state = models.JSONField(default=dict)  # Store game state
    status = models.CharField(max_length=10, default='waiting')  # waiting, playing, finished

class DiceRoll(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    roll_value = models.IntegerField()
    player = models.ForeignKey(OPUser, on_delete=models.CASCADE)
"""