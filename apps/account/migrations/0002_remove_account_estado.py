# Generated by Django 3.0.4 on 2020-04-29 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='estado',
        ),
    ]
