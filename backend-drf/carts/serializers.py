from rest_framework import serializers
from .models import Cart, CartItem

# for classiteam
class CartItemSerializer(serializers.ModelSerializer):
  product_name = serializers.CharField(source="product.name")
  class Meta:
    model = CartItem
    fields = "__all__"
    # dont create a separte cartitem view or api cause cart is already created do use nested here




class CartSerializer(serializers.ModelSerializer):
  # nested serializer here items is used because in cartserializer related field used is item
  items = CartItemSerializer(many=True)
  # always do that outside the class meta
  class Meta:
    model = Cart
    fields = "__all__"
