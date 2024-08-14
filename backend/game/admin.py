from django.contrib import admin
from .models import *

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'player1', 'player2', 'current_turn', 'status')
    list_filter = ('status', 'player1', 'player2')
    search_fields = ('player1__username', 'player2__username', 'status')

@admin.register(DiceRoll)
class DiceRollAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'roll_value', 'player')
    list_filter = ('game', 'player')
    search_fields = ('game__id', 'player__username')