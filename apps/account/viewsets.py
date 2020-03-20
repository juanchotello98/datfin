from rest_framework import viewsets
from apps.account.models import Account
from .serializer import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer