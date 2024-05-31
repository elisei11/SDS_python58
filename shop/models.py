from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

# class Customer(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=10, unique=True)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#
#     class Meta:
#         ordering = ['user']
#         verbose_name = 'customer'
#         verbose_name_plural = 'customers'
#
#     def __str__(self):
#         return self.user.username
