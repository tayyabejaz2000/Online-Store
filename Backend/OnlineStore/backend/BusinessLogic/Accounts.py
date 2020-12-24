from django.http.response import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .tokenHandler import ObtainToken
from ..models import BillingAddress, CartProducts, Product, Shop, UserAccount, Cart
from ..serializers import AccountsSerializer


class Accounts:
    def login_user(self):
        return ObtainToken.as_view()

    def create_user(self, user_data):
        serializer = AccountsSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.save()
                user_cart = Cart(user=user)
                user_cart.save()
                return None
        raise Exception("Couldn't Create User with data: " + str(user_data))

    def logout_user(self, refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError as e:
            raise Exception("Invalid Token, [Refresh Token]:" +
                            str(refresh_token) + ", [Exception]:" + str(e))
        except:
            raise Exception("Couldn't Logout User, [Refresh Token]:" +
                            str(refresh_token))

    def getAccount(self, id):
        return UserAccount.objects.get(id=id)


class User:
    def addBillingAddress(self, user, billingAddress):
        try:
            address = BillingAddress(user=user,
                                     billingAddress=billingAddress)
            address.save()
        except:
            raise Exception("Couldn't add address for User, [Address]:" +
                            str(billingAddress))

    # Adan Start

    def addProductToCart(self, user, product_id, quantity):
        try:
            cart = Cart.objects.get(user=user)
            product = Product.objects.get(id=product_id)
            CartEntry = CartProducts(
                cart=cart, product=product, quantity=quantity)
            CartEntry.save()
        except:
            raise Exception("Unable to add Product to Cart, [Product_ID]: " +
                            str(product_id))

    # Adan End


class Vendor:
    def setShop(self, vendor, shop_name, shop_location):
        try:
            shop = Shop(vendor=vendor, shop_name=shop_name,
                        location=shop_location)
            shop.save()
        except:
            raise Exception("Couldn't add Shop for Vendor, [Shop Name]:" +
                            str(shop_name) + ", [Shop Location]:" + str(shop_location))

    def addProduct(self, shop, product_name, product_desc, quantity):
        try:
            product = Product(name=product_name, description=product_desc,
                              stock=quantity, shop=shop)
            product.save()
        except:
            raise Exception("Couldn't add Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(quantity))

    def removeProduct(self, product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
        except:
            raise Exception("Couldn't delete Product: [Product ID]:" +
                            str(product_id))

    # Adan Work
    def getAllProducts(self):
        products = list(Product.objects.all().values())
        return products

    def updateProduct(self, product_id, product_name, product_desc, product_quantity):
        try:
            product = Product.objects.get(pk=product_id)
            product.name = product_name
            product.description = product_desc
            product.stock = product_quantity
            product.save()
        except:
            raise Exception("Couldn't update Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(product_quantity))
