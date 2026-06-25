from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


# imagine cart like a bag when we add the product in the cart it becomes cartitem
# will be creating two mod Cart and Cartitems
class Cart(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
   
  def __str__(self):
    return self.user.email

# cartitem is nothing but the product which is there inside the cart  
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)

  def __str__(self):
    return f"{self.product.name} x {self.quantity}" 
  # Apple x 3
  