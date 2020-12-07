from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import BillingAddress, Product, Shop, UserAccount, Cart


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ('groups', 'user_permissions',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password is not None:
            instance.set_password(password)
        return instance
