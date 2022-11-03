# Generated by Django 4.1.1 on 2022-11-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do Aluno')),
                ('primeira_nota', models.IntegerField(verbose_name='1º Bimestre')),
                ('segunda_nota', models.IntegerField(verbose_name='2º Bimestre')),
                ('terceira_nota', models.IntegerField(verbose_name='3º Bimestre')),
                ('quarta_nota', models.IntegerField(verbose_name='4º Bimestre')),
                ('media_notas', models.IntegerField(blank=True, default=0, verbose_name='Média')),
            ],
        ),
    ]
