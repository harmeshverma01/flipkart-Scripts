
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)  
    
    def __str__(self) -> str:
        return self.name  
    


class Product(models.Model):
    name = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='category', null=True )
    
    def __str__(self) -> str:
        return self.name
    
    
    
