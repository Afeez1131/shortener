# Generated by Django 3.1.1 on 2020-10-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiz', '0003_auto_20201011_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='fizzurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='fizzurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
