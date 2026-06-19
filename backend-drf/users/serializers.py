# we hve creted to convert complex data into querysets and json data
from rest_framework import serializers
from django.contrib.auth import get_user_model
# came from admin.py file where we have imported the user model using get_user_model() function

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  # write_only = True means that the password will not be returned in the response but it will be used to create the user and hash the password
  class Meta:
    model = User
    fields = ['id','email', 'username', 'password']

    # now we want the pass hashing so we use the inbulid crete func
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    # for normal but not good partice
    # user = User.objects.create_user(
    #   validated_data['email'],
    #   validated_data['username'],)
    return user

    # ** it is key word arg take whtever field are coming recursively and cretae the user all the 
      # so this is the inbulid create func which will create the user and hash the password just extend the modelss.ModelSerializer and then we can use the create func
      

# after login what should we see
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','email', 'username','first_name','last_name']