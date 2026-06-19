from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserSerializer
# for basic we use apiview but major thing would be done through serializers 
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
# only accese pl we see the profike so its private

# data will come back in form of post request since we r saving  it
class RegisterView(APIView):
  def post(self, request):
    # we need to import the serializer which we have created in the serializers.py file of the user app
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ProfileView(APIView):
  permission_classes = [IsAuthenticated]  # only authenticated user can access this view
  def get(self, request):
    serializer = UserSerializer(request.user)
    # request.data first we used to wirte this but since of the permission class we can directly use the request.user to get the user data
    return Response(serializer.data)