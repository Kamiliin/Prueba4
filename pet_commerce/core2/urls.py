from django.urls import path
from core2.views import lista_pets, detalle_pets
from api.views import CustomAuthToken

urlpatterns = [
    path('lista_pets', lista_pets, name="lista_pets"),
    path('detalle_pets/<id>', detalle_pets, name="detalle_pets"),
    path('token/', CustomAuthToken.as_view(), name="token")
]
