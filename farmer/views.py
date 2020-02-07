from rest_framework import viewsets

from farmer.models import Farmer
from farmer.serializer import FarmerSerializer


class FarmerView(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
