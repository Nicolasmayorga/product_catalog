from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.mail import send_mail


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_admin = True
        super().save(*args, **kwargs)


class Product(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)

    def has_changed(self, old_instance):
        if not old_instance:
            return True
        return (old_instance.sku != self.sku or 
                old_instance.name != self.name or 
                old_instance.price != self.price or 
                old_instance.brand != self.brand)

    def save(self, *args, **kwargs):
            if self.pk:
                original = Product.objects.get(pk=self.pk)
                if self.has_changed(original):
                    send_mail(
                        'Producto modificado',
                        f'El producto {self.name} ha sido modificado.',
                        'from@example.com',
                        ['to@example.com'],  
                        fail_silently=False,
                    )

            super().save(*args, **kwargs)


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product',)
