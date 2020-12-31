from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.contrib.auth.hashers import make_password, check_password


class AccountModel(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True)
    user_type = models.CharField(max_length=2, default='B', null=False, choices=[
        ('S', 'Seller'),  # Normal Seller
        ('B', 'Buyer'),  # Normal Buyere
        ('E', 'Employee'),  # Employee working in Store, can solve complaints
        ('A', 'Admin'),  # Admins can add/remove any account(employee, seller, buyer)
    ])

    class Meta:
        indexes = [
            models.Index(fields=['username', ]),
            models.Index(fields=['email', ]),
        ]


class BillingAddressModel(models.Model):
    buyer = models.ForeignKey(AccountModel, on_delete=models.CASCADE,
                              limit_choices_to={'user_type': 'B'}, related_name='billing_addresses')
    billingAddress = models.CharField(max_length=512, null=False)

    class Meta:
        unique_together = ('buyer', 'billingAddress')

    def __str__(self):
        return self.buyer.username


class WalletModel(models.Model):
    user = models.OneToOneField(AccountModel, on_delete=models.CASCADE,
                                related_name='wallet')
    balance = models.PositiveIntegerField(default=0)
    wallet_password = models.CharField(max_length=128, null=True, default=None)

    def set_password(self, password: str):
        self.wallet_password = make_password(password)

    def check_password(self, password: str):
        return check_password(password, self.wallet_password)


class ShopModel(models.Model):
    seller = models.OneToOneField(
        AccountModel, on_delete=models.CASCADE, limit_choices_to={'user_type': 'S'}, related_name='shop')
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ':' + self.seller.username


class CategoryModel(models.Model):
    name = models.CharField(max_length=20, primary_key=True)


class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0,
                                           validators=[MaxValueValidator(100)])
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE,
                             null=False, related_name='products')
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, null=False, related_name='products')
    isRemoved = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ":" + self.category.name


class CartModel(models.Model):
    buyer = models.OneToOneField(AccountModel, on_delete=models.CASCADE,
                                 limit_choices_to={'user_type': 'B'}, related_name='cart')
    products = models.ManyToManyField(ProductModel, through='CartProductModel',
                                      through_fields=('cart', 'product',))

    def __str__(self):
        return self.buyer.username


class CartProductModel(models.Model):
    cart = models.ForeignKey(
        CartModel, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)

    class Meta:
        unique_together = ('cart', 'product')


class InvoiceModel(models.Model):
    net = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0,
                                           validators=[MaxValueValidator(100)])


class OrderModel(models.Model):
    buyer = models.ForeignKey(AccountModel, on_delete=models.CASCADE,
                              limit_choices_to={'user_type': 'B'}, related_name='orders')
    created_on = models.DateTimeField(auto_now_add=True)
    invoice = models.OneToOneField(
        InvoiceModel, on_delete=models.CASCADE, related_name='order')
    ordered_products = models.ManyToManyField(ProductModel, through='OrderedProductModel',
                                              through_fields=('order', 'product', ))

    address = models.ForeignKey(BillingAddressModel, on_delete=models.CASCADE,
                                related_name='shippings')


class OrderedProductModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE,
                              related_name='products')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,
                                related_name='orders')
    quantity = models.IntegerField(null=False, default=1)

    status = models.CharField(max_length=2, default='P', null=False, choices=[
        ('P', 'Placed'),
        ('S', 'Shipped'),
        ('C', 'Completed'),
        ('R', 'Returned'),
    ])

    class Meta:
        unique_together = ('order', 'product')


class ComplaintModel(models.Model):
    complaint_body = models.CharField(max_length=512)
    answer_body = models.CharField(max_length=512, null=True, default=None)
    user = models.ForeignKey(AccountModel, on_delete=models.CASCADE,
                             related_name='complaints')
    lookup_employee = models.ForeignKey(AccountModel, on_delete=models.CASCADE, null=True, default=None,
                                        limit_choices_to={'user_type': 'E'}, related_name='lookup_complaints')


class ReviewModel(models.Model):
    stars = models.PositiveIntegerField(default=0,
                                        validators=[MaxValueValidator(5)])
    feedback = models.CharField(max_length=512)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,
                                related_name='reviews')
    buyer = models.ForeignKey(AccountModel, on_delete=models.CASCADE,
                              related_name='reviews')
