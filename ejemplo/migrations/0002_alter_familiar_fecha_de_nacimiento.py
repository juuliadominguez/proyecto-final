# Generated by Django 4.1.3 on 2022-12-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
    ]