# Generated by Django 4.1 on 2022-08-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_profile_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]
