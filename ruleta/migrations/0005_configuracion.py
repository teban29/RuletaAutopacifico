# Generated by Django 5.1.1 on 2024-11-27 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruleta', '0004_premio_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probabilidad_no_ganar', models.FloatField(default=30)),
            ],
        ),
    ]
