from rest_framework import viewsets

from product.models import Product
from product.serializer import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
