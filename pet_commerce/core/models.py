from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class CustomUser(AbstractBaseUser):
    username = None
    name = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Correo', unique=True)
    comments = models.TextField('Comentarios')

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")

    def __str__(self):
        return f'{self.name} - {self.email}'


class Category(models.Model):
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = ("Categoría")
        verbose_name_plural = ("Categorías")

    def __str__(self):
        return f'{self.id} - {self.name}'


class Product(models.Model):
    sku = models.CharField('SKU', max_length=50)
    name = models.CharField('Nombre', max_length=50)
    price = models.CharField('Precio', max_length=50)
    stock = models.CharField('Stock disponible', max_length=50)
    desc = models.CharField('Descripción', max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoría')

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return f'{self.id} - {self.sku} - {self.name}'
