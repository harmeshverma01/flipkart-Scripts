from cart.utils import product_details, html_content, get_next_page
from .serializers import Categoryserializer, Productserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product
import json
# Create your views here.

class ProductView(APIView):
    serializer_class = Categoryserializer

  
    def get(self, request, id=None):
        product = Product.objects.all()
        rating = request.GET.get('rating', None)
        category = request.GET.get('category', None)
        if rating is not None and category is not None:
            product = product.filter(rating=rating, category=category)
        serializer = Productserializer(product, many=True)
        return Response(serializer.data)
  
  
    def post(self, request, ):
        try:
            name = request.GET.get('name', None)
            category = Category.objects.get(name=name)
        except Category.DoesNotExist:
            category = Category.objects.create(
                name=name
            )
            category.save()
            
        url = "https://www.flipkart.com/search?q="+ name
       
        soup = html_content(url)
    
        while True:
            divs = soup.find_all("div",{"class": "_2kHMtA"})
            list_of_product = product_details(divs, list_of_product=[])
            for product in list_of_product:
                product['category'] = category
                soup = html_content(url)
                print(product)
                serializer = Productserializer(data=product)
                if not serializer.is_valid():
                    return Response(serializer.errors)
                serializer.save()
            return Response({"details": "fetched"})
            