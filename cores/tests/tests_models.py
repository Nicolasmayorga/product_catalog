import pytest
from django.contrib.auth import get_user_model
from cores.models import Product, ProductView

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="testuser", password="testpass123")
    assert user.username == "testuser"
    assert user.is_admin == False
    assert user.is_superuser == False
    assert user.check_password("testpass123")

@pytest.mark.django_db
def test_create_admin_user():
    user = User.objects.create_superuser(username="testadmin", password="testpass123")
    assert user.username == "testadmin"
    assert user.is_admin == True
    assert user.is_superuser == True
    assert user.check_password("testpass123")

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(sku="12345", name="Test Product", price="9.99", brand="Test Brand")
    assert product.sku == "12345"
    assert product.name == "Test Product"
    assert product.price == "9.99"
    assert product.brand == "Test Brand"

@pytest.mark.django_db
def test_product_view():
    product = Product.objects.create(sku="12345", name="Test Product", price="9.99", brand="Test Brand")
    product_view = ProductView.objects.create(product=product, view_count=5)
    assert product_view.product == product
    assert product_view.view_count == 5
