from rest_framework import generics
from .models import Product, User, ProductView
from .serializers import ProductSerializer, UserSerializer, ProductViewSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        product = self.get_object()
        view, created = ProductView.objects.get_or_create(product=product)
        if not created:
            view.view_count += 1
            view.save()
            
        response = super().get(request, *args, **kwargs)
        return response
    
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductAnalyticsView(generics.ListAPIView):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    
    def get_queryset(self):
        return super().get_queryset().order_by('view_count')