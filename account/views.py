from django.shortcuts import render
from rest_framework import viewsets

from account.models import Account
from account.serializer import AccountSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
