# Generated by Django 4.2.2 on 2023-06-20 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_medidaspaciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospaciente',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medidaspaciente',
            name='data',
            field=models.DateField(),
        ),
    ]