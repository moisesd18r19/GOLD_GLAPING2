# Generated by Django 5.0.1 on 2024-02-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.IntegerField(unique=True),
        ),
    ]
