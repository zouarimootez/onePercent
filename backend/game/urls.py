from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, DiceRollViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'dice-rolls', DiceRollViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
