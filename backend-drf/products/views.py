from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.
class CategoryListView(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  # we use the listview because it we need to just list the objects the other funcs, or classes or maxins r lenghty so this brongs directly

class ProductListView(generics.ListAPIView):
  queryset = Product.objects.filter(is_active=True)
  serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
  queryset = Product.objects.filter(is_active=True)
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  # we r using retriveapi because we want only one product 
