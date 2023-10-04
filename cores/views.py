from rest_framework import generics
from .models import Product, User, ProductView
from .serializers import ProductSerializer, UserSerializer, ProductViewSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_HEADER, TYPE_STRING


token_param = Parameter(
    name="Authorization",
    in_=IN_HEADER,
    description="Token de autenticación en formato 'Bearer {token}'",
    type=TYPE_STRING,
    required=True
)


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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(operation_description="Listado de productos y creación de un nuevo producto.",
                        responses={200: ProductSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny]
        self.check_permissions(request)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Crear un nuevo producto.",
                        request_body=ProductSerializer,
                        responses={201: ProductSerializer()},
                        manual_parameters=[token_param])
    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)
        return super().post(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(operation_description="Obtener detalles de un producto específico.",
                        responses={200: ProductSerializer()})
    def get(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny]
        self.check_permissions(request)
        
        product = self.get_object()
        view, created = ProductView.objects.get_or_create(product=product)
        if not created:
            view.view_count += 1
            view.save()
        response = super().get(request, *args, **kwargs)
        return response

    @swagger_auto_schema(operation_description="Actualizar un producto existente por completo.",
                        request_body=ProductSerializer,
                        responses={200: ProductSerializer()},
                        manual_parameters=[token_param])
    def put(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Actualizar parcialmente un producto existente.",
                        request_body=ProductSerializer,
                        responses={200: ProductSerializer()},
                        manual_parameters=[token_param])
    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Eliminar un producto.",
                        responses={204: 'Producto eliminado correctamente.'},
                        manual_parameters=[token_param])
    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)
        return super().delete(request, *args, **kwargs)



class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="Listado de usuarios.",
                        responses={200: UserSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny]
        self.check_permissions(request)
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Crear un nuevo usuario.",
                        request_body=UserSerializer,
                        responses={201: UserSerializer()},
                        manual_parameters=[token_param])
    def post(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny]
        self.check_permissions(request)
        return super().post(request, *args, **kwargs)



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="Obtener detalles de un usuario específico.",
                        responses={200: UserSerializer()},
                        manual_parameters=[token_param])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Actualizar un usuario existente por completo.",
                        request_body=UserSerializer,
                        responses={200: UserSerializer()},
                        manual_parameters=[token_param])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Actualizar parcialmente un usuario existente.",
                        request_body=UserSerializer,
                        responses={200: UserSerializer()},
                        manual_parameters=[token_param])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Eliminar un usuario.",
                        responses={204: 'Usuario eliminado correctamente.'},
                        manual_parameters=[token_param])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ProductAnalyticsView(generics.ListAPIView):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_description="Obtener estadísticas/análisis de productos ordenados por número de vistas.",
                        responses={200: ProductViewSerializer(many=True)},
                        manual_parameters=[token_param])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().order_by('-view_count')
