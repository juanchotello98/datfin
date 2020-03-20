from django.db import models
from apps.budget.models import Budget
# Create your models here.

class Category(models.Model):
	nombre = models.CharField(max_length=30, null=True)
	planeado = models.IntegerField()
	actual = models.IntegerField()
	diferencia = models.IntegerField()
	presupuesto = models.ForeignKey(Budget, on_delete=models.CASCADE)

	def __str__(self):
		return ("%s "%(self.nombre))