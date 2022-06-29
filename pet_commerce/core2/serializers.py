from rest_framework import serializers
from core.models import Product 
# CustomUser, Category,#


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'price', 'stock','desc','category']



