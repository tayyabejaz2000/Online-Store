from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.contrib.auth.hashers import make_password, check_password


class UserAccount(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True)
    user_type = models.CharField(max_length=2, default='U', null=False, choices=[
        ('V', 'Vendor'),  # Normal Vendor
        ('U', 'User'),  # Normal User
        ('E', 'Employee'),  # Employee working in Store, can solve complaints
        ('A', 'Admin'),  # Admins can add/remove any account(employee, vendor, user)
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


class Wallet(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE,
                                limit_choices_to={'user_type': ['U', 'V']}, related_name='wallet')
    balance = models.PositiveIntegerField(default=0)
    wallet_password = models.CharField(max_length=128, null=True, default=None)

    def set_password(self, password: str):
        self.wallet_password = make_password(password)

    def check_password(self, password: str):
        return check_password(password, self.wallet_password)


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
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
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


class Invoice(models.Model):
    net = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0,
                                           validators=[MaxValueValidator(100)])

    @property
    def total(self):
        return self.net - (self.net * (self.discount/100))


class Order(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                                limit_choices_to={'user_type': 'U'}, related_name='orders')
    created_on = models.DateTimeField(auto_now_add=True)
    invoice = models.OneToOneField(
        Invoice, on_delete=models.CASCADE, related_name='order')
    ordered_products = models.ManyToManyField(Product, through='OrderedProduct',
                                              through_fields=('order', 'product', ))


class Shipping(models.Model):
    status = models.CharField(max_length=2, default='P', null=False, choices=[
        ('P', 'Placed'),
        ('S', 'Shipped'),
        ('C', 'Completed'),
        ('R', 'Returned'),
    ])
    address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE,
                                related_name='shippings')


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='orders')
    quantity = models.IntegerField(null=False, default=1)

    shipping = models.OneToOneField(Shipping, on_delete=models.CASCADE,
                                    related_name='OrderedProduct')

    class Meta:
        unique_together = ('order', 'product')


class Complaint(models.Model):
    complaint_body = models.CharField(max_length=512)
    answer_body = models.CharField(max_length=512, null=True, default=None)
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE,
                                limit_choices_to={'user_type': ['U', 'V']}, related_name='complaints')
    lookup_employee = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, default=None,
                                        limit_choices_to={'user_type': 'E'}, related_name='lookup_complaints')


class Review(models.Model):
    stars = models.PositiveIntegerField(default=0,
                                        validators=[MaxValueValidator(5)])
    feedback = models.CharField(max_length=512)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
