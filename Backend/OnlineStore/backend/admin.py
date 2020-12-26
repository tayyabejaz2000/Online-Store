from django.contrib import admin
from .models import CategoryModel, ComplaintModel, InvoiceModel, OrderModel, OrderedProductModel, ReviewModel, AccountModel, CartModel, ProductModel, ShopModel, BillingAddressModel, CartProductModel, WalletModel


admin.site.register(AccountModel)
admin.site.register(CartModel)
admin.site.register(ProductModel)
admin.site.register(ShopModel)
admin.site.register(BillingAddressModel)
admin.site.register(CartProductModel)
admin.site.register(OrderModel)
admin.site.register(OrderedProductModel)
admin.site.register(CategoryModel)
admin.site.register(WalletModel)
admin.site.register(InvoiceModel)
admin.site.register(ComplaintModel)
admin.site.register(ReviewModel)
