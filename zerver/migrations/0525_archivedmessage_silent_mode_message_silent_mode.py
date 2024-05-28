# Generated by Django 5.0.6 on 2024-05-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0524_realmuserdefault_enable_dm_silent_mode_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="archivedmessage",
            name="silent_mode",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="message",
            name="silent_mode",
            field=models.BooleanField(default=False),
        ),
    ]
