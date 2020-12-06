from django.contrib import admin
from .models import UserAccount, Cart, Product


class AccountsAdmin(admin.ModelAdmin):
    model = UserAccount


class CartsAdmin(admin.ModelAdmin):
    model = Cart


class ProductsAdmin(admin.ModelAdmin):
    model = Product


admin.site.register(UserAccount, AccountsAdmin)
admin.site.register(Cart, CartsAdmin)
admin.site.register(Product, ProductsAdmin)
