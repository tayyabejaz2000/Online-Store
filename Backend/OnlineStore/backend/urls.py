from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AddProductToCart, GetAccountDetails, GetAllCategories, GetAllProducts, GetBillingAddresses, GetCartProducts, GetProduct, GetSellerProducts, GetUserData, Login, OrderCart, Signup, Logout, AddBillingAddress, AddProduct, EditShop, RemoveProduct, UpdateCart, UpdateProduct

urlpatterns = [
    # login and get token
    path('login/', Login.as_view()),
    # refresh from token
    path('refresh/', TokenRefreshView.as_view()),
    # sign up/create new user
    path('signup/', Signup.as_view()),
    # logout
    path('logout/', Logout.as_view()),



    path('products/', GetAllProducts.as_view()),
    path('products/categories', GetAllCategories.as_view()),
    path('products/get-product', GetProduct.as_view()),
    path('products/add-product', AddProduct.as_view()),
    path('products/remove-product', RemoveProduct.as_view()),
    path('products/update-product', UpdateProduct.as_view()),

    path('account/min-data', GetUserData.as_view()),
    path('account/data', GetAccountDetails.as_view()),

    path('user/cart', GetCartProducts.as_view()),
    path('user/place-order', OrderCart.as_view()),
    path('user/add-to-cart', AddProductToCart.as_view()),
    path('user/update-cart', UpdateCart.as_view()),
    path('user/add-billing-address', AddBillingAddress.as_view()),
    path('user/get-billing-addresses', GetBillingAddresses.as_view()),

    path('seller/products', GetSellerProducts.as_view()),
    path('seller/set-shop', EditShop.as_view()),
]
