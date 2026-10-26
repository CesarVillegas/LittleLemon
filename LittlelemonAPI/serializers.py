from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal


# class menuItemSerializer(serializers.ModelSerializer):
#    id = serializers.IntegerField()
#    title = serializers.CharField(max_length=255)
#    price = serializers.DecimalField(max_digits=6, decimal_places=2)
#    inventory = serializers.IntegerField()

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class menuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField()
    category = categorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_with_tax', 'category']
        
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')