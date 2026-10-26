from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal


# class menuItemSerializer(serializers.ModelSerializer):
#    id = serializers.IntegerField()
#    title = serializers.CharField(max_length=255)
#    price = serializers.DecimalField(max_digits=6, decimal_places=2)
#    inventory = serializers.IntegerField()
   

class menuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_with_tax']
        
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')