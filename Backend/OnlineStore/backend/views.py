from rest_framework import permissions
from rest_framework.views import APIView
from .BusinessLogic.Controller import Store

# Views just forward all calls to Controller

controller = Store()


class Login:
    def as_view(self):
        return controller.login_user()


class Signup(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        return controller.create_user(request)


class Logout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        return controller.logout_user()


class AddBillingAddress(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        return controller.addBillingAddress(request)


class SetShop(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        return controller.setShop(self, request)


class AddProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        return controller.addProduct(request)


class RemoveProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        return controller.removeProduct(request)

# {"username":"vendor1","email":"vendor1@gmail.com","password":"myPassword","phone_number":"03208519958","user_type":"V"}
