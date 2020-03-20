# Generated by Django 2.1.7 on 2020-03-20 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planeado', models.IntegerField()),
                ('actual', models.IntegerField()),
                ('diferencia', models.IntegerField()),
                ('presupuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.Budget')),
            ],
        ),
    ]
