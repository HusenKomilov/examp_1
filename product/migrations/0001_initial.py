# Generated by Django 4.2.7 on 2024-03-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("price", models.DecimalField(decimal_places=3, max_digits=6)),
                ("marja", models.DecimalField(decimal_places=3, max_digits=10)),
                ("package_code", models.CharField(max_length=32)),
                ("encrypted_price", models.BinaryField()),
                ("encrypted_marja", models.BinaryField()),
                ("encrypted_code", models.BinaryField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]