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
    
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        product = self.get_object()
        ProductView.objects.create(product=product) # Incrementa view count
        return super().get(request, *args, **kwargs)

class ProductAnalyticsView(generics.ListAPIView):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    
    def get_queryset(self):
        return super().get_queryset().order_by('-view_count')