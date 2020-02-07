from rest_framework import serializers

from farmer.models import Farmer
from store.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'phone_number', 'region', 'city', 'account_id', 'user_id')
