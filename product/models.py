from unicodedata import category
from uuid import uuid4
# from django.db import models
from djongo import models

# Create your models here.

class Product(models.Model):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stock = models.IntegerField()
    active = models.BooleanField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    create_at = models.DateField(auto_now_add=True)



#     {
#   "id" : UUIDField
#   "name" : "string",
#   "category" : "string",
#   "brand" : "string",
#   "description": "string",
#   "stock" : integer,
#   "active" : true,
#   "image" : multipart/form-data
#   "rating" : integer,
#   "price" : BigDecimal
# } 