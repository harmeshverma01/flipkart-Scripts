from .models import Category, Product
from rest_framework import serializers


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    
class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'    