# Generated by Django 4.1.6 on 2023-03-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='coast',
            field=models.FloatField(default=0),
        ),
    ]
