from datetime import date
from rest_framework import permissions, status
from rest_framework.response import Response
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
        try:
            controller.create_user(request.data)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.logout_user(request.data["refresh_token"])
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetUserData(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            userdata = controller.getUserData(request.data.id)
            return Response(data=userdata, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Throw: ", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddBillingAddress(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.addBillingAddress(request.data.id, request.data.address)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class SetShop(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.setShop(request.data.id, request.data.shop_name,
                               request.data.shop_location)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.addProduct(request.data.id, request.data.product_name,
                                  request.data.product_desc, int(request.data.quantity))
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class RemoveProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.removeProduct(request.data.product_id)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetAllProducts(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            products = controller.getAllProducts()
            return Response(data=products,  status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class UpdateProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.updateProduct(request.data.product_id, request.data.product_name,
                                     request.data.product_desc, request.data.quantity)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddProductToCart(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            controller.addProductToCart(
                request.data.id, request.data.product_id, request.data.quantity)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
