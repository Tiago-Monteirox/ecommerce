# Generated by Django 4.1.4 on 2022-12-23 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('produto', '0005_alter_produto_preco_marketing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria'),
            preserve_default=False,
        ),
    ]