# Generated by Django 2.0 on 2018-03-07 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0042_auto_20180302_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2018, 3, 7, 8, 53, 6, 991237), verbose_name='Ημερομηνία'),
        ),
    ]