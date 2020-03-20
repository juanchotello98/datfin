from apps.transaction.models import Transaction
from rest_framework import serializers, fields


class TransactionSerializer(serializers.ModelSerializer):
	fecha = serializers.DateField(format="%Y-%m-%d")
	class Meta: 
		model = Transaction
		fields = '__all__'