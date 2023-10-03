from django.contrib import admin

# Register your models here.
from .models import Product, User, ProductView

admin.site.register(Product) 
admin.site.register(User)

@admin.register(ProductView)
class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('product', 'view_count')
    list_filter = ('product',)
    search_fields = ('product__name',)
