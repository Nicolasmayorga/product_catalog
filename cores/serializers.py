from rest_framework import serializers
from .models import Product, User, ProductView


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(source='is_superuser')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin']


class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = ['id', 'product', 'view_count']
