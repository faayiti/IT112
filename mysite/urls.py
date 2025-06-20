from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django site!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),  # Your app URLs
    path('', home),  # Root URL now shows home view
=======
from django.urls import path
from home.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
>>>>>>> 25fdc67203d91020c137d588539dd90955daa92d
]
