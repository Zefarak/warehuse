# Generated by Django 2.0 on 2017-12-27 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0028_auto_20171224_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 27, 7, 52, 33, 819303), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]