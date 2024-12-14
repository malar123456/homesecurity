# Generated by Django 5.1.2 on 2024-10-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_smokedata_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_value', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ObjectData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_value', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]