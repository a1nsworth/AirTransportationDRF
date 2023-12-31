# Generated by Django 5.0 on 2023-12-21 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("available_cities", "0001_initial"),
        ("client", "0005_client_departure_city"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="arrival_city",
        ),
        migrations.RemoveField(
            model_name="client",
            name="arrival_date",
        ),
        migrations.RemoveField(
            model_name="client",
            name="departure_city",
        ),
        migrations.RemoveField(
            model_name="client",
            name="departure_date",
        ),
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
                ("departure_date", models.DateField(default=None, null=True)),
                ("arrival_date", models.DateField(default=None, null=True)),
                (
                    "arrival_city",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client_arrival_city",
                        to="available_cities.availablecities",
                    ),
                ),
                (
                    "departure_city",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client_departure_city",
                        to="available_cities.availablecities",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="client",
            name="order",
            field=models.OneToOneField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client",
                to="client.clientorder",
            ),
        ),
    ]
