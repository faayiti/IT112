from django.http import JsonResponse
from .models import Item
import json

def home(request):
    return HttpResponse("Welcome to the API homepage.")

def all_items(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False, content_type="application/json")

def single_item(request):
    item_id = request.GET.get('id')
    try:
        item = Item.objects.get(id=item_id)
        return JsonResponse({
            'id': item.id,
            'name': item.name,
            'description': item.description
        }, content_type="application/json")
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, content_type="application/json")

def create_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = Item.objects.create(name=data['name'], description=data['description'])
            return JsonResponse({'success': True, 'id': item.id}, status=200, content_type="application/json")
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=200, content_type="application/json")
    return JsonResponse({'error': 'Invalid request'}, content_type="application/json")
