from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .tokenHandler import ObtainToken
from ..models import Shop, UserAccount, Cart, Wallet
from ..serializers import AccountsSerializer


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
                    if (user.user_type == 'U' or user.user_type == 'V'):
                        wallet = Wallet(user=user)
                        wallet.set_password(user_data.wallet_password)
                        wallet.save()
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
