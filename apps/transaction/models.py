from django.db import models
from apps.account.models import Account
from apps.category.models import Category
# Create your models here.

class Transaction(models.Model):
	fecha = models.DateField()
	descripcion = models.CharField(max_length=50)
	valor = models.IntegerField()
	cuenta = models.ForeignKey(Account, on_delete= models.CASCADE)
	categoria = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
	tipo = models.CharField(max_length=20)
