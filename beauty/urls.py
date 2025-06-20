from django.urls import path
from . import views

urlpatterns = [
    path('', views.beauty_list, name='beauty_list'),
    path('<int:item_id>/', views.beauty_detail, name='beauty_detail'),
]
