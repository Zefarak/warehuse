# Generated by Django 2.0 on 2017-12-28 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transcations', '0008_auto_20171223_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixedcostinvoice',
            old_name='price',
            new_name='final_price',
        ),
    ]