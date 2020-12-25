from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .tokenHandler import ObtainToken
from ..models import BillingAddress, CartProduct, Category, Product, Shop, UserAccount, Cart
from ..serializers import AccountsSerializer


# class account:

#     class Meta:
#         model = UserAccount

#     def __init__(self, *args, **kwargs):
#         self.account_data = None
#         if isinstance(args[0], dict):
#             serializer = AccountsSerializer(data=args[0])
#             if serializer.is_valid():
#                 validated_data = serializer.validated_data
#                 password = validated_data.pop('password', None)
#                 instance = self.Meta.model(**validated_data)
#                 if password is not None:
#                     instance.set_password(password)
#                 self.account_data = instance
#         else:
#             self.account_data = self.Meta.model(args, kwargs)

#     def save(self):
#         self.account_data.save()

#     def getAccount(self):
#         return self.account_data


class accounts:

    def login_user(self):
        return ObtainToken.as_view()

    def create_user(self, user_data):
        serializer = AccountsSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                try:
                    user.save()
                    if (user.user_type == 'U'):
                        user_cart = Cart(user=user)
                        user_cart.save()
                    elif (user.user_type == 'V'):
                        shop = Shop(vendor=user, shop_name=user_data.shop_name,
                                    location=user_data.shop_location)
                        shop.save()
                    return None
                except:
                    raise Exception("Couldn't Create User with data: " +
                                    str(user_data))
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


class user:

    def __init__(self, account):
        self.account = account

    def addBillingAddress(self, billingAddress):
        try:
            address = BillingAddress(user=self.account,
                                     billingAddress=billingAddress)
            address.save()
        except:
            raise Exception("Couldn't add address for User, [Address]:" +
                            str(billingAddress))

    def getCart(self):
        return self.account.cart

    def addProductToCart(self, product, quantity):
        try:
            cart = self.getCart()
            CartEntry = CartProduct(
                cart=cart, product=product, quantity=quantity)
            CartEntry.save()
        except:
            raise Exception("Unable to add Product to Cart")


class vendor:

    def __init__(self, account):
        self.account = account

    def editShop(self, shop_name, shop_location):
        try:
            shop = self.account.shop
            shop.name = shop_name
            shop.location = shop_location
            shop.save()
        except:
            raise Exception("Couldn't add Shop for Vendor, [Shop Name]:" +
                            str(shop_name) + ", [Shop Location]:" + str(shop_location))

    def getShop(self):
        return self.account.shop


class products:
    def getProduct(self, product_id):
        return Product.objects.get(pk=product_id)

    def getCategory(self, category_id):
        return Category.objects.get(name=category_id)

    def getAllProducts(self):
        return list(Product.objects.filter(isRemoved=False))

    def addProduct(self, product_name, product_desc, quantity, category, shop):
        try:
            _category = self.getCategory(category)
            product = Product(name=product_name, description=product_desc,
                              stock=quantity, shop=shop, category=_category)
            product.save()
        except:
            raise Exception("Couldn't add Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(quantity))

    def updateProduct(self, product_id, product_name, product_desc, product_quantity, category):
        try:
            product = self.getProduct(product_id)
            product.name = product_name
            product.description = product_desc
            product.stock = product_quantity
            product.category = self.getCategory(category)
            product.save()
        except:
            raise Exception("Couldn't update Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_desc) + ", [Quantity]:" + str(product_quantity))

    def removeProduct(self, product_id):
        try:
            product = self.getProduct(product_id)
            product.isRemoved = True
            product.save()
        except:
            raise Exception("Couldn't delete Product: [Product ID]:" +
                            str(product_id))


class cart:
    pass
