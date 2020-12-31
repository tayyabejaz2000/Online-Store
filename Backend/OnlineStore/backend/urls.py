from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AddComplaint, AddProductToCart, AddReview, CancelOrderItem, GetAccountDetails, GetAllCategories, GetAllProducts, GetBillingAddresses, GetCartProducts, GetComplaints, GetOrders, GetProduct, GetSellerProducts, GetShop, GetUserData, Login, OrderCart, ResolveComplaint, ReturnItem, Signup, Logout, AddBillingAddress, AddProduct, EditShop, RemoveProduct, UpdateCart, UpdateProduct

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
    path('products/add-review', AddReview.as_view()),

    path('account/min-data', GetUserData.as_view()),
    path('account/data', GetAccountDetails.as_view()),

    path('user/cart', GetCartProducts.as_view()),
    path('user/orders', GetOrders.as_view()),
    path('user/add-complaint', AddComplaint.as_view()),
    path('user/place-order', OrderCart.as_view()),
    path('user/cancel-item', CancelOrderItem.as_view()),
    path('user/return-item', ReturnItem.as_view()),
    path('user/add-to-cart', AddProductToCart.as_view()),
    path('user/update-cart', UpdateCart.as_view()),
    path('user/add-billing-address', AddBillingAddress.as_view()),
    path('user/get-billing-addresses', GetBillingAddresses.as_view()),

    path('seller/products', GetSellerProducts.as_view()),
    path('seller/shop', GetShop.as_view()),
    path('seller/edit-shop', EditShop.as_view()),

    path('employee/complaints', GetComplaints.as_view()),
    path('employee/complaints/resolve', ResolveComplaint.as_view()),
]
