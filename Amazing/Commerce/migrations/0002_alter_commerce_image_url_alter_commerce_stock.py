# Generated by Django 4.1.7 on 2023-03-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commerce',
            name='image_url',
            field=models.CharField(max_length=2803),
        ),
        migrations.AlterField(
            model_name='commerce',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
