# cores/urls.py

from django.urls import path
from .views import (
    ProductListView, 
    ProductDetailView,
    UserListView,
    UserDetailView
)

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),

    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()) 
]