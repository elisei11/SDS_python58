from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # dummy_field = models.CharField(max_length=10, default='dummy')
