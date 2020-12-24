from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AddProductToCart, GetAllProducts, GetUserData, Login, Signup, Logout, AddBillingAddress, AddProduct, SetShop, RemoveProduct, UpdateProduct

urlpatterns = [
    # login and get token
    path('login/', Login().as_view()),
    # refresh from token
    path('refresh/', TokenRefreshView.as_view()),
    # sign up/create new user
    path('signup/', Signup.as_view()),
    # logout
    path('logout/', Logout.as_view()),



    path('products/', GetAllProducts.as_view()),

    path('account/data', GetUserData.as_view()),

    path('user/add-to-cart', AddProductToCart.as_view()),
    path('user/add-billing-address', AddBillingAddress.as_view()),

    path('vendor/set-shop', SetShop.as_view()),
    path('vendor/add-product', AddProduct.as_view()),
    path('vendor/remove-product', RemoveProduct.as_view()),
    path('vendor/update-product', UpdateProduct.as_view()),
]
