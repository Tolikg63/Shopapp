from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Docstring for Product
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    # @property
    # def description_short(self):
    #     if len(self.description) < 40:
    #         return self.description
    #     else:
    #         return self.description[:40] + '...'

    def __str__(self):
        return self.name


class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')