# Generated by Django 2.0 on 2019-04-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='snacks',
            field=models.ManyToManyField(related_name='drinks', to='inventory_manager.Snack'),
        ),
    ]
