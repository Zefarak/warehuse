# Generated by Django 2.0 on 2018-02-27 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0037_auto_20180227_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 9, 24, 51, 103113), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]