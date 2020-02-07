from rest_framework import serializers

from financial_institution.models import FinancialInstitution


class FinancialInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInstitution
        fields = ('id', 'name', 'phone_number', 'region', 'city', 'account_id', 'user_id')
