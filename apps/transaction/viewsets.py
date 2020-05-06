from rest_framework import viewsets
from apps.transaction.models import Transaction
from apps.transaction.serializer import TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['usuario']