"""pet_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from core.views import (
    DeleteCategoryView,
    index,
    CreateUserView,
    ListProductsView,
    CreateProductView,
    CreateCategoryView,
    DeleteProductView,
    ListCategoriesView,
    EditCategoryView,
    EditProductView,
    DogStoreView,
    CatStoreView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('dog_store/', DogStoreView.as_view(), name='dog_store'),
    path('cat_store/', CatStoreView.as_view(), name='cat_store'),
    path('registros/product/', ListProductsView.as_view(), name='list_products'),
    path('registros/product/create/',
         CreateProductView.as_view(), name='create_product'),
    path('registros/product/edit/<int:pk>/',
         EditProductView.as_view(), name='edit_product'),
    path('registros/product/delete/<int:pk>/',
         DeleteProductView.as_view(), name='delete_product'),
    path('registros/category/', ListCategoriesView.as_view(), name='list_categories'),
    path('registros/category/create/',
         CreateCategoryView.as_view(), name='create_category'),
    path('registros/category/edit/<int:pk>/',
         EditCategoryView.as_view(), name='edit_category'),
    path('registros/category/delete/<int:pk>/',
         DeleteCategoryView.as_view(), name='delete_category'),
    path('api/', include('core2.urls'))     
]


