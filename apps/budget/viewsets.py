from rest_framework import viewsets
from apps.budget.models import Budget
from apps.budget.serializer import BudgetSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BudgetViewSet(viewsets.ModelViewSet):
	queryset = Budget.objects.all()
	serializer_class = BudgetSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['usuario']