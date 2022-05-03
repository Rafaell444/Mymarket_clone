from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(default="yourphoto.jpeg", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return self.name
