# Generated by Django 2.0.7 on 2018-08-16 14:09

from django.db import migrations


def criar_parametro_inicial(apps, schema_editor):
    ParameterForBase = apps.get_model('core', 'ParameterForBase')
    parametro = ParameterForBase.objects.first()

    if not parametro:
        parametro = ParameterForBase()
        parametro.nomeProjeto = "Core"
        parametro.tituloProjeto = "Prefeitura de Palmas"
        parametro.descricaoProjeto = "Aqui faz uma descrição do sistema."
        parametro.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_parametro_inicial)
    ]
