# Generated by Django 3.2.8 on 2021-10-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0006_alter_leccion_idprofesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='apellido_profesor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='leccion',
            name='nombre_leccion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='contrasenia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
