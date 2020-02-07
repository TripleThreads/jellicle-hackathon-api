from rest_framework import serializers

from farmer.models import Farmer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'status', 'price')
