# Generated by Django 2.0 on 2019-04-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='snacks',
            field=models.ManyToManyField(to='inventory_manager.Snack'),
        ),
    ]
