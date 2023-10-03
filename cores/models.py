from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions'
    )

class Product(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)

class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)