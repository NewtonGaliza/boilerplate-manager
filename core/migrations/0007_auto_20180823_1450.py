# Generated by Django 2.0.7 on 2018-08-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180823_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterforbase',
            name='descricaoProjeto',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='parameterforbase',
            name='iconeProjeto',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='parameterforbase',
            name='nomeProjeto',
            field=models.TextField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='parameterforbase',
            name='tituloProjeto',
            field=models.TextField(blank=True, default='', max_length=200, null=True),
        ),
    ]
