# Generated by Django 4.0.6 on 2022-08-19 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgapp', '0037_alter_order_orderdate_alter_payment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 19, 16, 4, 763218)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 19, 19, 16, 4, 764219), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdat',
            field=models.DateField(default=datetime.datetime(2022, 8, 19, 19, 16, 4, 762218)),
        ),
    ]
