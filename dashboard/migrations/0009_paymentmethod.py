# Generated by Django 2.0.2 on 2018-04-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20180107_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('site_active', models.BooleanField(default=False)),
            ],
        ),
    ]