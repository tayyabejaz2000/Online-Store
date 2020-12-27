from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class ObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, format='json'):
        token = super().get_token(user)
        return token


class ObtainToken(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer


class JWTAccountHandeling():
    @staticmethod
    def login_account():
        return ObtainToken.as_view()

    @staticmethod
    def logout_account(refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError as e:
            raise Exception("Invalid Token, [Refresh Token]:" +
                            str(refresh_token) + ", [Exception]:" + str(e))
        except:
            raise Exception("Couldn't Logout User, [Refresh Token]:" +
                            str(refresh_token))
