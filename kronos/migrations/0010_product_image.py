# Generated by Django 5.0.3 on 2024-04-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kronos", "0009_remove_product_sale_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
