from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    phone_number = models.CharField(max_length=12)
    billingAddress = models.CharField(blank=True, max_length=512)
    user_type = models.CharField(max_length=2, default='U', choices=[
        ('V', 'Vendor'),
        ('U', 'User'),
        ('A', 'Admin'),
    ])
    REQUIRED_FIELDS = ['email', 'password', 'phone_number', 'first_name']

    class Meta:
        indexes = [
            models.Index(fields=['username', ]),
            models.Index(fields=['email', ]),
        ]


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Cart(models.Model):
    user_id = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
