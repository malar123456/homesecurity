# Generated by Django 5.1.2 on 2024-10-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smokedata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
