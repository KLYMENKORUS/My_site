# Generated by Django 4.1 on 2022-08-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_tags"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="post",
            managers=[],
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("draft", "DRAFT"), ("published", "PUBLISHED")],
                default="published",
                max_length=10,
            ),
        ),
    ]
