# Generated by Django 5.0 on 2023-12-22 13:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flight", "0004_remove_flightcomposition_stewardess_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="flightcomposition",
            old_name="pilot",
            new_name="pilot_main",
        ),
    ]
