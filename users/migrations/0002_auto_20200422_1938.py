# Generated by Django 3.0.5 on 2020-04-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='active',
            field=models.BooleanField(default=True, verbose_name='is an active'),
        ),
    ]