from rest_framework import viewsets
from .serializers import *
from .models import *

class GameViewSet(viewsets.ModelViewSet):
    print("GameViewSet loaded")
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class DiceRollViewSet(viewsets.ModelViewSet):
    queryset = DiceRoll.objects.all()
    serializer_class = DiceRollSerializer