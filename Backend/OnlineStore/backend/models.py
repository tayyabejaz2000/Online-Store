from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True)
    user_type = models.CharField(max_length=2, default='U', null=False, choices=[
        ('V', 'Vendor'),
        ('U', 'User'),
        ('A', 'Admin'),
    ])

    class Meta:
        indexes = [
            models.Index(fields=['username', ]),
            models.Index(fields=['email', ]),
        ]


class BillingAddress(models.Model):
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, limit_choices_to={'user_type': 'U'})
    billingAddress = models.CharField(max_length=512, null=False)


class Shop(models.Model):
    vendor = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, limit_choices_to={'user_type': 'V'})
    shop_name = models.CharField(max_length=30)
    location = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False)


class Cart(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, through='CartProducts', through_fields=('cart', 'product',))


class CartProducts(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='product_quantity')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_quantity')
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        unique_together = ('cart', 'product')

# Rest tables
