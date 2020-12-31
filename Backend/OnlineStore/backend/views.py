from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .BLL.Controller import Store


# Views just forward all calls to Controller
controller = Store()


class Login:
    def as_view():
        return controller.login_account()


class Signup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            controller.create_account(request.data)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class EditAccount(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.editUser(request.user.id, request.data["username"], request.data.get("password", None),
                                request.data["email"], request.data["last_name"], request.data["last_name"],
                                request.data["phone_number"], request.data.get("wallet_password", None))
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            controller.logout_account(request.data.refresh_token)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetUserData(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            userdata = controller.getAccountData(request.user.id)
            return Response(data=userdata, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Throw: ", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetAccountDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            userdetails = controller.getAccountDetails(request.user.id)
            return Response(data=userdetails, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Throw: ", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddBillingAddress(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.addBillingAddress(
                request.user.id, request.data["address"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetBillingAddresses(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            billing_addresses = controller.getBillingAddresses(request.user.id)
            return Response(data=billing_addresses, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class EditShop(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.editShop(request.user.id, request.data["shop_name"],
                                request.data["shop_location"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetShop(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            shopData = controller.getShop(request.user.id)
            return Response(data=shopData, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.addProduct(request.user.id,
                                  request.data["product_name"],
                                  request.data["product_desc"],
                                  int(request.data["quantity"]),
                                  int(request.data["price"]),
                                  int(request.data["discount"]),
                                  request.data["category"]
                                  )
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            product = controller.getProduct(request.data["product_id"])
            return Response(data=product, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class RemoveProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.removeProduct(request.data["product_id"])
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Exception Thrown: ", e)  # Log error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetAllProducts(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            products = controller.getAllProducts()
            return Response(data=products,  status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class UpdateProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.updateProduct(request.data["product_id"],
                                     request.data["product_name"],
                                     request.data["product_desc"],
                                     int(request.data["quantity"]),
                                     int(request.data["price"]),
                                     int(request.data["discount"]),
                                     request.data["category"]
                                     )
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddProductToCart(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.addProductToCart(
                request.user.id, request.data["product_id"], request.data["quantity"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class UpdateCart(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.updateCart(
                request.user.id, request.data["product_id"], request.data["quantity"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetSellerProducts(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            products = controller.getSellerProducts(request.user.id)
            return Response(data=products, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetAllCategories(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            categories = controller.getAllCategories()
            return Response(data=categories, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetCartProducts(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            products = controller.getCartProducts(request.user.id)
            return Response(data=products, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class OrderCart(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.placeOrder(
                request.user.id, request.data["billing_address"], request.data["discount"], request.data["wallet_password"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class CancelOrderItem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.cancelOrderItem(
                request.user.id, request.data["ordered_product_id"])
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetOrders(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            orders = controller.getOrders(request.user.id)
            return Response(data=orders, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddReview(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.addReview(request.user.id, request.data["product_id"],
                                 request.data["stars"], request.data["feedback"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddComplaint(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.addComplaint(request.user.id,
                                    request.data["complaint_body"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class ReturnItem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.returnItem(
                request.user.id, request.data["ordered_product_id"])
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class GetComplaints(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            complaints = controller.getUnresolvedComplaints()
            return Response(data=complaints, status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class ResolveComplaint(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.resolveComplaint(request.data["complaint_id"], request.user.id,
                                        request.data["response"])
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class AddBalance(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            controller.addBalance(request.user.id, request.data["amount"],
                                  request.data["wallet_password"])
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("Exception Thrown", e)  # Log Error
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
