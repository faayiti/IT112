from django.shortcuts import render, get_object_or_404
from .models import BeautyItem

def beauty_list(request):
    items = BeautyItem.objects.all()
    return render(request, 'beauty/list.html', {'items': items})

def beauty_detail(request, item_id):
    item = get_object_or_404(BeautyItem, pk=item_id)
    return render(request, 'beauty/detail.html', {'item': item})
