from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),             # <-- This line added for homepage
    path('items/', views.all_items),
    path('item/', views.single_item),
    path('add-item/', views.create_item),
]
