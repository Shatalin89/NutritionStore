from django.db import models
from django.contrib.auth.models import User


class brand(models.Model):
    brand_name = models.CharField(max_length=64)
    brand_site = models.URLField(null=True)

class type(models.Model):
    type_name = models.CharField(max_length=64)

class products(models.Model):
    products_name = models.CharField(max_length=64)
    products_brand = models.ForeignKey(brand)
    products_type = models.ForeignKey(type)
    products_price = models.IntegerField(default=0)
    products_count = models.IntegerField(default=0)

class product_image(models.Model):
    image_product = models.ForeignKey(products)
    image = models.ImageField(upload_to='/media/')

class raiting(models.Model):
    raiting_product = models.ForeignKey(products)
    raiting_stars = models.IntegerField(default=5)
    raiting_user = models.ForeignKey(User)

