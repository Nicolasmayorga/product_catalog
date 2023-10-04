from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    UserListView,
    UserDetailView,
    ProductAnalyticsView,
    login
)

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('product-analytics/', ProductAnalyticsView.as_view()),
    path('login/', login, name='login')
]
