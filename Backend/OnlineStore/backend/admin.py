from django.contrib import admin
from .models import Category, Complaint, Invoice, Order, OrderedProduct, Review, Shipping, UserAccount, Cart, Product, Shop, BillingAddress, CartProduct, Wallet


admin.site.register(UserAccount)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(BillingAddress)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(OrderedProduct)
admin.site.register(Category)
admin.site.register(Wallet)
admin.site.register(Invoice)
admin.site.register(Shipping)
admin.site.register(Complaint)
admin.site.register(Review)
