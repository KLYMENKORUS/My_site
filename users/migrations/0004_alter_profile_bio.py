# Generated by Django 4.1 on 2022-08-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(max_length=500),
        ),
    ]
