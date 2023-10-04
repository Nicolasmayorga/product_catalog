from rest_framework import generics
from .models import Product, User, ProductView
from .serializers import ProductSerializer, UserSerializer, ProductViewSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class ProductListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser] 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser] 
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
