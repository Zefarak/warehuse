# Generated by Django 2.0 on 2017-12-22 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0023_auto_20171222_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 12, 22, 15, 23, 32, 798245)),
        ),
    ]