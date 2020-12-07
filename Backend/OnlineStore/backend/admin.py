from django.contrib import admin
from .models import UserAccount, Cart, Product, Shop, BillingAddress, CartProducts


class AccountsAdmin(admin.ModelAdmin):
    model = UserAccount


class CartsAdmin(admin.ModelAdmin):
    model = Cart


class ProductsAdmin(admin.ModelAdmin):
    model = Product


class ShopAdmin(admin.ModelAdmin):
    model = Shop


class BillingAddressAdmin(admin.ModelAdmin):
    model = BillingAddress


class CartProductsAdmin(admin.ModelAdmin):
    model = CartProducts


admin.site.register(UserAccount, AccountsAdmin)
admin.site.register(Cart, CartsAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(CartProducts, CartProductsAdmin)
