# Generated by Django 4.1.4 on 2022-12-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DispModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=100, unique=True)),
                ('local', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=400)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('bits', models.CharField(max_length=50)),
                ('horario', models.DateTimeField()),
                ('timestamp', models.IntegerField()),
                ('addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='controle_opd.dispmodel')),
            ],
        ),
    ]
