# Generated by Django 3.0.6 on 2020-09-17 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20200917_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestpost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]