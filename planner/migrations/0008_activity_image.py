# Generated by Django 5.0.8 on 2024-08-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planner", "0007_add_lat_long_to_itinerary_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="image",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
