from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default="yourphoto.jpeg", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=9, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def validate(self, data):
        data['created'] = data['created'].replace(second=0, microsecond=0)
        data['updated'] = data['updated'].replace(second=0, microsecond=0)

        return data

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self):
        return self.name
