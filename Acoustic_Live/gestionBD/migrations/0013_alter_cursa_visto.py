# Generated by Django 3.2.8 on 2021-11-06 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0012_cursa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursa',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
