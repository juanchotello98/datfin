from django.db import models
from apps.account.models import Account
from apps.category.models import Category
from apps.user.models import User
from django.utils import timezone
# Create your models here.

class Transaction(models.Model):
	fecha = models.DateField()
	descripcion = models.CharField(max_length=50)
	valor = models.IntegerField()
	cuenta = models.ForeignKey(Account, on_delete= models.CASCADE)
	categoria = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	tipo = models.CharField(max_length=20)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)