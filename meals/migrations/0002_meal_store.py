# Generated by Django 3.0.5 on 2020-04-22 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meals', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Store'),
        ),
    ]
