# Generated by Django 2.0 on 2017-12-22 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manager', '0025_auto_20171222_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='day_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 12, 22, 23, 7, 20, 817316), verbose_name='Ημερομηνία'),
        ),
    ]