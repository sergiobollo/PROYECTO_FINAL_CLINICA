# Generated by Django 3.2.dev20201112141917 on 2020-11-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
