# Generated by Django 5.0.1 on 2024-01-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_customuser_first_name_customuser_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
