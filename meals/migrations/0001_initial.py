# Generated by Django 3.0.5 on 2020-04-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slugname', models.SlugField(max_length=120, unique=True)),
                ('description', models.TextField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='meal price')),
                ('picture', models.ImageField(blank=True, help_text='Price max up to $999.99', null=True, upload_to='meals/pictures/', verbose_name='meal picture')),
                ('rating', models.FloatField(default=5.0, help_text="Meal's rating based on client califications")),
            ],
            options={
                'verbose_name': 'meal',
                'ordering': ('slugname',),
            },
        ),
    ]