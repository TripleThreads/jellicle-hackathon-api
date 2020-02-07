from rest_framework import viewsets

from financial_institution.models import FinancialInstitution
from financial_institution.serializer import FinancialInstitutionSerializer


class FinancialInstitutionView(viewsets.ModelViewSet):
    queryset = FinancialInstitution.objects.all()
    serializer_class = FinancialInstitutionSerializer
