from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal
import bleach


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
    # category = categorySerializer()
    category = categorySerializer(read_only = True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_with_tax', 'category', 'category_id']
        
    # def validate_title(self, value):
    #     print("ANTES:", repr(value))
    #     cleaned = bleach.clean(value)
    #     print("DESPUÉS:", repr(cleaned))
    #     return cleaned
        # return bleach.clean(value)
        
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])

        if attrs['price'] < 2:
            raise serializers.ValidationError({'price': 'Price should not be less than 2.0'})

        if attrs['inventory'] < 0:
            raise serializers.ValidationError({'stock': 'Stock cannot be negative'})

        return super().validate(attrs)
        
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('1.1')
    
    # def validate(self, attrs):
    #     attrs['title'] = bleach.clean(attrs['title'])
    #     if(attrs['price']<2):
    #         raise serializers.ValidationError('Price should not be less than 2.0')
    #     if(attrs['inventory']<0):
    #         raise serializers.ValidationError('Stock cannot be negative')
    #     return super().validate(attrs)