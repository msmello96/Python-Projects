# Generated by Django 4.2.1 on 2023-05-13 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_criador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='cor_principals',
            new_name='cor_principal',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='descicao',
            new_name='descricao',
        ),
    ]
