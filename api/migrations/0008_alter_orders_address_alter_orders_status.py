# Generated by Django 4.1.2 on 2023-01-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_products_carts_product_carts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('order-placed', 'order-placed'), ('despathed', 'despatched'), ('in-transit', 'in-transit'), ('cancelled', 'cancelled')], default='order-placed', max_length=200),
        ),
    ]
