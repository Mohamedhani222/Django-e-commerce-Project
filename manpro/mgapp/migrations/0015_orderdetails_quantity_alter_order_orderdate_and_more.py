# Generated by Django 4.0.6 on 2022-08-12 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgapp', '0014_alter_order_orderdate_alter_product_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 18, 39, 9, 917792)),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdat',
            field=models.DateField(default=datetime.datetime(2022, 8, 12, 18, 39, 9, 916792)),
        ),
    ]