from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

@admin.register(OPUser)
class OPUserAdmin(BaseUserAdmin):
    model = OPUser
    list_display = ('username', 'opusername', 'flous', 'diamond')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('opusername', 'oppassword', 'flous', 'diamond')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'opusername', 'oppassword', 'flous', 'diamond', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
"""
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('player1', 'player2', 'current_turn', 'status')

@admin.register(DiceRoll)
class DiceRollAdmin(admin.ModelAdmin):
    list_display = ('game', 'roll_value', 'player')
"""