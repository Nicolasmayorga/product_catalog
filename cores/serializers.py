from rest_framework import serializers
from .models import Product, User, ProductView

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'is_admin']
        
# serializer para porduct ProductView
class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = '__all__'
