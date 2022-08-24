from .models import Category, Product
from rest_framework import serializers


class productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    
class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'    