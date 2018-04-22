# Generated by Django 2.0 on 2018-04-19 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0052_auto_20180326_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 19, 18, 28, 56, 129332), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='retailorderitem',
            name='day_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='retailorderitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Μονάδας Με έκπτωση.'),
        ),
        migrations.AlterField(
            model_name='retailorderitem',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]