from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer
from rest_framework.response import Response

# Create your views here.
class CartListView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)
    # if created:  #it is a boolean value true/false
    #   print('cart created')
    # we can use to send mail to user that acc is created
# to add to the cart the user should already be login so we r using permission class
