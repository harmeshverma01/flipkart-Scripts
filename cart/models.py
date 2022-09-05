from unicodedata import name
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, null=True, blank=False)  
    
    # def __str__(self) -> str:
    #     return self.name  


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    descriptions = models.TextField()
    price = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)
    
    def approved(self):
        self.approved = True
        self.save() 
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
