from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.user} {self.created_at}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} {self.quantity} {self.price}"

