# Generated by Django 4.1.4 on 2022-12-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_alter_subcategoria_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='subcategoria',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='SubCategoria',
        ),
    ]
