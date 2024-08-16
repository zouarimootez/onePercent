from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response



"""
class GameViewSet(viewsets.ModelViewSet):
    print("GameViewSet loaded")
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class DiceRollViewSet(viewsets.ModelViewSet):
    queryset = DiceRoll.objects.all()
    serializer_class = DiceRollSerializer

"""
class OPUserViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            user = OPUser.objects.get(pk=pk)
            serializer = OPUserSerializer(user)
            return Response(serializer.data)
        except OPUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=404)