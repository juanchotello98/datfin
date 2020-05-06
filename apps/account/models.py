from django.db import models
from django.utils import timezone
from apps.user.models import User
# Create your models here.

class Account(models.Model):
	nombre = models.CharField(max_length=25)
	saldo = models.IntegerField()
	tipo = models.CharField(max_length=20)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	
	def __str__(self):
		return ("%s "%(self.nombre))