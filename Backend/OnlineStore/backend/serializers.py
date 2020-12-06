from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserAccount, Cart


# Get Token from Username and Password
class ObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user, format='json'):
        token = super(ObtainTokenSerializer, cls).get_token(user)
        token['username'] = user.username
        token['account-type'] = user.user_type
        # Add custom claims if u want
        return token


# User Registration Class
class AccountsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField()
    email = serializers.EmailField(required=True)
    user_type = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
    )

    class Meta:
        accountmodel = UserAccount
        cartModel = Cart
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password', 'user_type',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.accountmodel(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        if instance.user_type == 'U':
            cartInstance = self.Meta.cartModel(user_id=instance.pk)
            cartInstance.save()
        return instance
