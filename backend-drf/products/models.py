from django.db import models
from decimal import Decimal
 
class Category(models.Model):
  cat_name = models.CharField(max_length=25)
  cat_desc = models.TextField(null=True, blank=True)
  
  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    # category was there so by using the verbose it is solved

  def __str__(self):
    return self.cat_name

# Create your models here. models we r in
class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
  #  # ForeignKey()because one to many relo cause product can have many

  # we r setting it to cascade because if the category is deleted then the product should also be deleted and blank=True
  image = models.ImageField(upload_to='products/',blank=True,null=True)
  # image upload in media files
  price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal)
  stock = models.PositiveIntegerField()

# positive integer field because we hve the stock is never negative so it can be either 0 or mor ethan that
  tax_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00')) 
  is_active = models.BooleanField(default=True)
# to show the active status
  created_at = models.DateTimeField(auto_now_add=True)
# auto_now_add is changed because once it is created it cant be changed 
  upadated_at = models.DateTimeField(auto_now=True)
# we can upadte those changes

  def __str__(self):
    return self.name

