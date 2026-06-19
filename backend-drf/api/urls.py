# we hve created a new app called api and we need to include the urls from that app in the main urls.py file
from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
  path('register/', UserViews.RegisterView.as_view()), 
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  #access tokens
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #refresh tokens,
  # we removed from the start of the token api
  path('profile/',UserViews.ProfileView.as_view()),  # include the profile view from the users app
]
# as_view is the the class based view which we have created in the views.py file of the user app