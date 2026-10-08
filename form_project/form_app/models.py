from django.db import models


from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    TYPES = [
        ('Vendor', 'Vendor'),
        ('Customer','Customer'),
    ]
    user_type = models.CharField(choices=TYPES, max_length=20, null=True)
    full_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.username}'

class CategoryModel(models.Model):
    name = models.CharField()

class ProductModel(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    qty = models.PositiveIntegerField(null=True)
    total_amount = models.FloatField(null=True)
    expired_date=models.DateField(null=True)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        related_name='product_category',
        null=True
    )
    created_by = models.ForeignKey(
        UserModel,
        on_delete= models.CASCADE,
        related_name='product_user',
        null=True
    )
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.product_name}'

