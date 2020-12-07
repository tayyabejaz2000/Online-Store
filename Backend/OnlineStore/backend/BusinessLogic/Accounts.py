from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .tokenHandler import ObtainToken
from ..models import BillingAddress, Product, Shop, UserAccount
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
                return None
        raise Exception("Exception")

    def logout_user(self, refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            raise Exception("Exception")

    def getAccount(self, id):
        return UserAccount.objects.get(id=id)


class User:
    def addBillingAddress(self, user, address):
        try:
            address = BillingAddress(
                user=user, billingAddress=address)
            address.save()
        except:
            raise Exception("Invalid Address")


class Vendor:
    def setShop(self, vendor, shop_name, shop_location):
        try:
            shop = Shop(vendor=vendor, shop_name=shop_name,
                        location=shop_location)
            shop.save()
        except:
            raise Exception("Invalid Shop")

    def addProduct(self, shop, product_name, product_desc):
        try:
            product = Product(name=product_name,
                              description=product_desc, shop=shop)
            product.save()
        except:
            raise Exception("Invalid Product")

    def removeProduct(self, product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
        except:
            raise Exception("Cant Delete Invalid Product")
