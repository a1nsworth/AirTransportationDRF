# Generated by Django 5.0 on 2023-12-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aircraft", "0006_remove_aircraftdescription_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircraftcharacteristic",
            name="capacity_peoples",
            field=models.PositiveSmallIntegerField(),
        ),
    ]
