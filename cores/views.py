from rest_framework import generics
from .models import Product, User, ProductView
from .serializers import ProductSerializer, UserSerializer, ProductViewSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProductViewListView(generics.ListCreateAPIView):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    
class ProductViewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer