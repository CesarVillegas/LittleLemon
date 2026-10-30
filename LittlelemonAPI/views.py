from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import MenuItem
from .serializers import menuItemSerializer
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

# class-based views
from rest_framework import viewsets

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializer
    ordering_fields=['price','inventory']
    ordering = ['id']                       # orden por defecto, quita el warning
    search_fields=['title','category__title']



@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        # items = MenuItem.objects.all()
        items = MenuItem.objects.select_related('category').all()
        # filtering
        category_name = request.query_params.get('category')
        to_price  = request.query_params.get('price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', 2)
        page = request.query_params.get('page', 1)
        
        if category_name:
            # items = items.filter(category__title=category_name)
            items = items.filter(category__title__iexact=category_name)
        if to_price:
            items = items.filter(price__lte=to_price) 
        if search:
            items = items.filter(title__icontains=search)
            # items = items.filter(title__istartswith=search)
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)
            # items = items.order_by(ordering)

        paginator = Paginator(items, per_page=perpage)
        # si el usuario pide una página que no existe, devolvemos un error 404
        try:
            items = paginator.page(page)
        except EmptyPage:
            items = []

        serialized_item = menuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = menuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)


@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = menuItemSerializer(item)
    return Response(serialized_item.data)