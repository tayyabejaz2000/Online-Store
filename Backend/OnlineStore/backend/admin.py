from django.contrib import admin
from .models import Category, Order, OrderedProduct, UserAccount, Cart, Product, Shop, BillingAddress, CartProduct


class AccountsAdmin(admin.ModelAdmin):
    model = UserAccount


class CartsAdmin(admin.ModelAdmin):
    model = Cart


class ProductsAdmin(admin.ModelAdmin):
    model = Product


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class ShopAdmin(admin.ModelAdmin):
    model = Shop


class BillingAddressAdmin(admin.ModelAdmin):
    model = BillingAddress


class CartProductAdmin(admin.ModelAdmin):
    model = CartProduct


class OrderAdmin(admin.ModelAdmin):
    model = Order


class OrderProductAdmin(admin.ModelAdmin):
    model = OrderedProduct


admin.site.register(UserAccount, AccountsAdmin)
admin.site.register(Cart, CartsAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedProduct, OrderProductAdmin)
admin.site.register(Category, CategoryAdmin)
