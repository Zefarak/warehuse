# Generated by Django 2.0 on 2018-01-07 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0035_auto_20171231_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 9, 1, 48, 705305), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]