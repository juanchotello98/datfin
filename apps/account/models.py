from django.db import models

# Create your models here.

class Account(models.Model):
	nombre = models.CharField(max_length=25)
	saldo = models.IntegerField()
	tipo = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)

	def __str__(self):
		return ("%s "%(self.nombre))