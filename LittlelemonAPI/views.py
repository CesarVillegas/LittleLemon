from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import menuItemSerializer
from django.shortcuts import get_object_or_404

@api_view()
def menu_items(request):
    # items = MenuItem.objects.all()
    items = MenuItem.objects.select_related('category').all()
    serialized_item = menuItemSerializer(items, many=True)
    return Response(serialized_item.data)


@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = menuItemSerializer(item)
    return Response(serialized_item.data)