# Generated by Django 5.0.3 on 2024-04-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kronos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sentiment",
            name="sentiment",
            field=models.CharField(
                blank=True,
                choices=[("POS", "Positive"), ("NEG", "Negative"), ("NEU", "Neutral")],
                max_length=3,
            ),
        ),
    ]