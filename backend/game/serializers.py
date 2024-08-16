from rest_framework import serializers
from .models import *
""""
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class DiceRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiceRoll
        fields = '__all__'"""


class OPUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPUser
        fields = ['username', 'flous', 'diamond']
