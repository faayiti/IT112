from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django site!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),  # Your app URLs
    path('', home),  # Root URL now shows home view
]
