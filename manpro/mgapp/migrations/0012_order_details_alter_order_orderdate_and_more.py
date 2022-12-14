# Generated by Django 4.0.6 on 2022-08-12 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgapp', '0011_alter_order_orderdate_alter_product_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='details',
            field=models.ManyToManyField(through='mgapp.OrderDetails', to='mgapp.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 17, 57, 19, 824734)),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdat',
            field=models.DateField(default=datetime.datetime(2022, 8, 12, 17, 57, 19, 824734)),
        ),
    ]
