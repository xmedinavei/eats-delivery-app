# Generated by Django 3.0.5 on 2020-04-22 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200422_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rider',
            old_name='rider_vehicle_licence_plate',
            new_name='licence_plate',
        ),
        migrations.RenameField(
            model_name='rider',
            old_name='rider_vehicle_made',
            new_name='vehicle_made',
        ),
        migrations.RenameField(
            model_name='rider',
            old_name='rider_vehicle_model',
            new_name='vehicle_model',
        ),
    ]