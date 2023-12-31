# Generated by Django 5.0 on 2023-12-20 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("available_cities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientOrder",
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
                (
                    "arrival_city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client_order_arrival_city",
                        to="available_cities.availablecities",
                    ),
                ),
                (
                    "departure_city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client_order_departure_city",
                        to="available_cities.availablecities",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("first_name", models.CharField(max_length=30)),
                ("phone_number", models.CharField(max_length=12)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("telegram_id", models.CharField(max_length=100, null=True)),
                (
                    "client_order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_client_order_id",
                        to="client.clientorder",
                    ),
                ),
            ],
        ),
    ]
