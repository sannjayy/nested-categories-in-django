from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

 
# Only Parent Categories View
class ParenCategoryView(APIView):
    def get(self, request):
        parent_cats = Category.objects.filter(parent__isnull=True)
        data = [{
                'id':cat.id,
                'name':cat.name,
                'slug':cat.slug
            } for cat in parent_cats]
        return response.Response(data)

# Category view
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

# Product View
class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer