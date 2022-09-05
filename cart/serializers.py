from .models import Category, Product
from rest_framework import serializers
    
    
class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'    
        
        
class Productserializer(serializers.ModelSerializer):
    # Category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name', 'price', 'rating', 'descriptions', 'category']
        
        def get_category(self,obj):
            objects = obj.name
            return objects      