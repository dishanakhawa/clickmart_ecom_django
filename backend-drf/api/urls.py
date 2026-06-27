# we hve created a new app called api and we need to include the urls from that app in the main urls.py file
from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from products import views as ProductViews
from carts import views as CartViews
from orders import views as OrderViews
urlpatterns = [
  path('register/', UserViews.RegisterView.as_view()), 
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  #access tokens
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #refresh tokens,
  # we removed from the start of the token api
  path('profile/',UserViews.ProfileView.as_view()),  # include the profile view from the users app

  # Categories api             
  path('categories/', ProductViews.CategoryListView.as_view()),

  # productlist api
  path('products/', ProductViews.ProductListView.as_view()),

# product detail api
  path('products/<int:pk>/', ProductViews.ProductDetailView.as_view()),

# carts api
  path('cart/', CartViews.CartView.as_view()),

  path('cart/add/', CartViews.AddToCartView.as_view()),

  # path('cart/items/<int:item_id>/', CartViews.ManageCartItemView.as_view()),
  path('cart/items/<int:item_id>/', CartViews.ManageCartItemView.as_view()),

  path('orders/place/', OrderViews.PlaceOrderView.as_view()),

  path('orders/', OrderViews.MyOrdersView.as_view()),

  path('orders/<int:pk>/', OrderViews.OrderDetailView.as_view()),
  

]
# as_view is the the class based view which we have created in the views.py file of the user app