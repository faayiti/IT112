from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),          # List all games
    path('<int:pk>/', views.game_detail, name='game_detail'),  # Detail of a game by ID
]
