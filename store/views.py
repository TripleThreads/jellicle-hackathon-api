from rest_framework import viewsets

from store.models import Store
from store.serializer import StoreSerializer


class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
