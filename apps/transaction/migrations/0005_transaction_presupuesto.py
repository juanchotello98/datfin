# Generated by Django 3.0.4 on 2020-05-09 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_budget_usuario'),
        ('transaction', '0004_auto_20200505_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='presupuesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget'),
        ),
    ]
