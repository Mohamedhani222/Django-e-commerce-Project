# Generated by Django 4.0.6 on 2022-08-14 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgapp', '0023_alter_order_orderdate_alter_payment_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='zip',
        ),
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 17, 51, 44, 377521)),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdat',
            field=models.DateField(default=datetime.datetime(2022, 8, 14, 17, 51, 44, 377521)),
        ),
    ]