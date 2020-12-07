from rest_framework import status
from rest_framework.response import Response
from ..models import UserAccount
from .Accounts import Accounts, User, Vendor


class Store:
    def login_user(self):
        return Accounts().login_user()

    def create_user(self, request):
        try:
            Accounts().create_user(request.data)
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def logout_user(self, request):
        try:
            Accounts().logout_user(request.data["refresh_token"])
            return Response(request.data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def addBillingAddress(self, request):
        try:
            user = Accounts().getAccount(request.data.id)
            User().addBillingAddress(user, request.data.address)
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def setShop(self, request):
        try:
            vendor = Accounts().getAccount(request.data.id)
            Vendor().setShop(vendor, request.data.shop_name, request.data.shop_location)
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def addProduct(self, request):
        try:
            vendor = Accounts().getAccount(request.data.id)
            Vendor().addProduct(vendor.shop, request.data.product_name,
                                request.data.product_desc, request.data.quantity)
            return Response(request.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def removeProduct(self, request):
        try:
            Vendor().removeProduct(request.data.product_id)
            return Response(request.data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
