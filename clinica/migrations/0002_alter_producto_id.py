# Generated by Django 3.2.dev20201112141917 on 2020-11-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]