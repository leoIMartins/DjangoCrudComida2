# Generated by Django 3.0.7 on 2020-06-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0003_auto_20200616_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='comida',
            name='valorCalorico',
            field=models.PositiveIntegerField(),
        ),
    ]
