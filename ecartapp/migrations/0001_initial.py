# Generated by Django 5.0.3 on 2024-04-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("price", models.FloatField()),
                ("pdetails", models.CharField(max_length=100)),
                ("cat", models.IntegerField()),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
