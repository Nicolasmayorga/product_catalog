import pytest
from cores.models import User, Product, ProductView
from cores.serializers import ProductSerializer, UserSerializer, ProductViewSerializer

@pytest.mark.django_db
def test_product_serializer():
    product = Product.objects.create(sku="12345", name="Test Product", price="9.99", brand="Test Brand")
    
    serializer = ProductSerializer(product)
    data = serializer.data

    assert data['sku'] == "12345"
    assert data['name'] == "Test Product"
    assert data['price'] == "9.99"
    assert data['brand'] == "Test Brand"


@pytest.mark.django_db
def test_user_serializer():
    user = User.objects.create_user(username="testuser", email="test@user.com", password="testpass123")
    serializer = UserSerializer(user)
    data = serializer.data

    assert data['id'] == user.id
    assert data['username'] == "testuser"
    assert data['email'] == "test@user.com"
    assert data['is_admin'] == False


@pytest.mark.django_db
def test_product_view_serializer():
    product = Product.objects.create(sku="12345", name="Test Product", price="9.99", brand="Test Brand")
    product_view = ProductView.objects.create(product=product, view_count=5)

    serializer = ProductViewSerializer(product_view)
    data = serializer.data

    assert data['id'] == product_view.id
    assert data['product'] == product.id
    assert data['view_count'] == 5
