# Generated by Django 5.0.4 on 2024-04-17 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphic_data',
            name='assists',
            field=models.IntegerField(default=None, verbose_name='asistencias del jugador'),
        ),
        migrations.AddField(
            model_name='graphic_data',
            name='damage',
            field=models.IntegerField(default=None, verbose_name='daño del jugador'),
        ),
        migrations.AddField(
            model_name='graphic_data',
            name='deaths',
            field=models.IntegerField(default=None, verbose_name='muertes del jugador'),
        ),
        migrations.AddField(
            model_name='graphic_data',
            name='experience',
            field=models.IntegerField(default=None, verbose_name='experiencia del jugador'),
        ),
        migrations.AddField(
            model_name='graphic_data',
            name='gold',
            field=models.IntegerField(default=None, verbose_name='oro del jugador'),
        ),
        migrations.AddField(
            model_name='graphic_data',
            name='kills',
            field=models.IntegerField(default=None, verbose_name='asesinatos del jugador'),
        ),
    ]
