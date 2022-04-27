from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=False
    )
    phone_field = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.user.username


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.FloatField(default=0.0)
    product_available_count = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images')

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", Kwargs={"pk": self.pk})

    def __str__(self):
        return self.name