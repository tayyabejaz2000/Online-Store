from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, format='json'):
        token = super().get_token(user)
        token['username'] = user.username
        token['accountType'] = user.user_type
        return token


class ObtainToken(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer
