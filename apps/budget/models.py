from django.db import models
from apps.user.models import User
from django.utils import timezone
# Create your models here.
class Budget(models.Model):
	nombre = models.CharField(max_length=30)
	mes = models.DateField(editable=False)
	total_planeado = models.IntegerField()
	total_actual =models.IntegerField()
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return ("%s "%(self.nombre))