# Generated by Django 4.2.3 on 2023-07-27 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_rename_categoria_categorias'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
    ]
