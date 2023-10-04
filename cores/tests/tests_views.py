import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from cores.models import Product, ProductView

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_login_view(api_client):
    User.objects.create_user(
        username="testuser", email="test@user.com", password="testpass123")

    response = api_client.post('/api/login/', {
        'username': 'testuser',
        'password': 'testpass123'
    })

    assert response.status_code == 200
    assert 'refresh' in response.data
    assert 'access' in response.data


@pytest.mark.django_db
def test_product_list_view(api_client):
    test_admin = User.objects.create_superuser(
        username="adminuser", email="admin@user.com", password="adminpass123")

    Product.objects.create(sku="12345", name="Test Product 1",
                        price="9.99", brand="Test Brand")
    Product.objects.create(sku="67890", name="Test Product 2",
                        price="19.99", brand="Test Brand")

    api_client.force_authenticate(user=test_admin)

    response = api_client.get('/api/products/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_list_view_unauthenticated(api_client):
    response = api_client.get('/api/products/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_product_create(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    product_data = {
        'sku': '99999',
        'name': 'New Test Product',
        'price': '49.99',
        'brand': 'New Brand'
    }
    response = api_client.post('/api/products/', data=product_data)
    assert response.status_code == 201  # Expecting Created status
    assert Product.objects.count() == 1


@pytest.mark.django_db
def test_product_create_unauthenticated(api_client):
    product_data = {
        'sku': '99999',
        'name': 'New Test Product',
        'price': '49.99',
        'brand': 'New Brand'
    }
    response = api_client.post('/api/products/', data=product_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_product_detail_view(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    product = Product.objects.create(
        sku="12345", name="Test Product 1", price="9.99", brand="Test Brand")
    response = api_client.get(f'/api/products/{product.pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_detail_view_unauthenticated(api_client):
    product = Product.objects.create(
        sku="12345", name="Test Product 1", price="9.99", brand="Test Brand")
    response = api_client.get(f'/api/products/{product.pk}/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_poduct_update(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    product = Product.objects.create(
        sku="12345", name="Test Product 1", price="9.99", brand="Test Brand")
    product_data = {
        'sku': '12345',
        'name': 'Updated Test Product',
        'price': '9.99',
        'brand': 'Test Brand'
    }
    response = api_client.put(
        f'/api/products/{product.pk}/', data=product_data)
    assert response.status_code == 200
    assert response.data['name'] == 'Updated Test Product'


@pytest.mark.django_db
def test_product_delete(api_client, admin_user):
    product = Product.objects.create(sku="12345", name="Test Product", price="9.99", brand="Test Brand")
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(f'/api/products/{product.id}/')
    assert response.status_code == 204
    assert Product.objects.count() == 0


@pytest.mark.django_db
def test_create_product_without_sku(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    product_data = {
        'name': 'New Test Product',
        'price': '49.99',
        'brand': 'New Brand'
    }
    response = api_client.post('/api/products/', data=product_data)
    assert response.status_code == 400
    assert 'sku' in response.data
    
    
@pytest.mark.django_db
def test_product_analytics_view(api_client):
    # SetUp
    test_admin = User.objects.create_superuser(username="adminuser", email="admin@user.com", password="adminpass123")
    product_1 = Product.objects.create(sku="12345", name="Test Product 1", price="9.99", brand="Test Brand")
    product_2 = Product.objects.create(sku="67890", name="Test Product 2", price="19.99", brand="Test Brand")
    
    ProductView.objects.create(product=product_1, view_count=5)
    ProductView.objects.create(product=product_2, view_count=10)

    # Autenticación
    api_client.force_authenticate(user=test_admin)
    
    # Acción
    response = api_client.get('/api/product-analytics/')
    
    # Afirmación
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['view_count'] == 10  # El producto con más visualizaciones debería estar primero
    assert response.data[1]['view_count'] == 5

