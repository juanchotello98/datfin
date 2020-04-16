from django.db import models

# Create your models here.
class Budget(models.Model):
	nombre = models.CharField(max_length=30)
	mes = models.DateField(editable=False)
	total_planeado = models.IntegerField()
	total_actual =models.IntegerField()
	estado = models.CharField(max_length=20) # Activo o Inactivo

	def __str__(self):
		return ("%s "%(self.nombre))