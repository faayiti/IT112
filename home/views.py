from django.shortcuts import render

def home_view(request):
    user_name = request.GET.get('user_name', '')  # Grab user_name query param
    return render(request, 'home/base.html', {'user_name': user_name})
