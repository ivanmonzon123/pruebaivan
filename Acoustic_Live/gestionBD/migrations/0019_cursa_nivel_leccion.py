# Generated by Django 3.2.8 on 2021-11-10 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0018_cursa_id_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursa',
            name='nivel_leccion',
            field=models.IntegerField(null=True),
        ),
    ]
