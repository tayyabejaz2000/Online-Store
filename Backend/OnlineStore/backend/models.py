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
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                             limit_choices_to={'user_type': 'U'}, related_name='billing_addresses')
    billingAddress = models.CharField(max_length=512, null=False)


class Shop(models.Model):
    vendor = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, limit_choices_to={'user_type': 'V'}, related_name='shop')
    shop_name = models.CharField(max_length=30)
    location = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             null=False, related_name='products')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, related_name='products')
    isRemoved = models.BooleanField(default=False)


class Cart(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE,
                                limit_choices_to={'user_type': 'U'}, related_name='cart')
    products = models.ManyToManyField(Product, through='CartProduct',
                                      through_fields=('cart', 'product',))


class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        unique_together = ('cart', 'product')


class Order(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                                limit_choices_to={'user_type': 'U'}, related_name='orders')
    created_on = models.DateTimeField(auto_now_add=True)
    ordered_products = models.ManyToManyField(Product, through='OrderedProduct',
                                              through_fields=('order', 'product', ))


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='orders')
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        unique_together = ('order', 'product')
