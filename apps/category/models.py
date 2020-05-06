from django.db import models
from apps.budget.models import Budget
from apps.user.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
	nombre = models.CharField(max_length=30, null=True)
	planeado = models.IntegerField()
	actual = models.IntegerField()
	diferencia = models.IntegerField()
	presupuesto = models.ForeignKey(Budget, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return ("%s "%(self.nombre))