# Generated by Django 3.2.dev20201112141917 on 2020-11-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0007_auto_20201115_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='lente',
        ),
        migrations.AddField(
            model_name='producto',
            name='izquierda_derecha',
            field=models.CharField(default='No aplica', max_length=64),
        ),
        migrations.AddField(
            model_name='producto',
            name='lejos_cerca',
            field=models.CharField(default='No aplica', max_length=64),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=64),
        ),
        migrations.AlterField(
            model_name='producto',
            name='armazon',
            field=models.BooleanField(default=False),
        ),
    ]
