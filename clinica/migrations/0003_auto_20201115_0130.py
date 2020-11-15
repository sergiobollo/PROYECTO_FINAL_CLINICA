# Generated by Django 3.2.dev20201112141917 on 2020-11-15 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_alter_producto_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo_de_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='forma_de_pago', to='clinica.formadepago'),
        ),
    ]
