from rest_framework import serializers

from farmer.models import Farmer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'full_name', 'phone_number', 'region', 'city', 'account_id', 'user_id')
