# Generated by Django 2.0.7 on 2018-08-01 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transacoes'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
