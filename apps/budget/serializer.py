from apps.budget.models import Budget
from rest_framework import serializers, fields


class BudgetSerializer(serializers.ModelSerializer):
	mes = serializers.DateField(format="%Y-%m-%d")
	class Meta: 
		model = Budget
		fields = '__all__'