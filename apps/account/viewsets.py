from rest_framework import viewsets
from apps.account.models import Account
from apps.account.serializer import AccountSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AccountViewSet(viewsets.ModelViewSet):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['usuario']