# Generated by Django 5.0.3 on 2024-04-21 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kronos", "0005_alter_product_cost_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
