# Generated by Django 2.2.7 on 2020-05-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Out wear'), ('P', 'Phones'), ('E', 'Electronics')], max_length=1),
        ),
    ]
