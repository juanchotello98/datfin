# Generated by Django 3.0.4 on 2020-04-26 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='saldo_actual_cuenta',
        ),
    ]
