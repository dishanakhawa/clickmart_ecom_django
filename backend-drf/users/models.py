from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#AbstractUser  = Add modify any field

# AbstractBaseUser = use this if we want to get the full control over your user model

#BaseUserManager = which carries call the actions over the user model Employee.objects = Manager => he is the one who carries the out all the actions over the user model like create_user, create_superuser, etc

# move step by step

# so now we just want to change the username to email => AbstractUser
class User(AbstractUser):
  email = models.EmailField(unique=True)

  USERNAME_FIELD = "email"
  # we want the email but still the django as a default wants the username 
  # so to avoid the default username extend # AbstractBaseUser
  # but since its only email changing we can use the AbstractUser which also follows the django protocols

  REQUIRED_FIELDS = ["username"]

  def __str__(self):
    return self.email
  # we only want the email to be changed the password we are not returning cuase its bydefault in the AbstractUser and we are not changing it so we can leave it as it is
