# Generated by Django 2.0.2 on 2018-05-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='big_banner',
            field=models.BooleanField(default=False),
        ),
    ]
