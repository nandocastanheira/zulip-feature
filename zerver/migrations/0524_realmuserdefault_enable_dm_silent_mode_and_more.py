# Generated by Django 5.0.6 on 2024-05-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0523_alter_multiuseinvite_subscribe_to_default_streams_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="realmuserdefault",
            name="enable_dm_silent_mode",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_dm_silent_mode",
            field=models.BooleanField(default=False),
        ),
    ]
