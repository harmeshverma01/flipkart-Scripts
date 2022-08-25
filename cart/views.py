from .utils import product_details, html_content, get_next_page
from .serializers import Categoryserializer, Productserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product

# Create your views here.

class ProductView(APIView):
    serializer_class = Categoryserializer

  
    def get(self, request, id=None):
        product = Product.objects.all()
        category = request.GET.get('category', None)
        rating = request.GET.get('rating', None)
        if category is not None or rating is not None:
            product = product.filter(category=category, rating=rating)
        serializer = self.serializer_class(product, many=True)
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
                url = get_next_page(url)
                if not url:
                    break
                soup = html_content(url)
                
                serializer = Productserializer(data=product)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
                