# Generated by Django 2.0 on 2018-06-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0002_auto_20180607_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='notes',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]