# Generated by Django 4.2.7 on 2024-03-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chats", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="is_archive",
            new_name="is_watched",
        ),
        migrations.RemoveField(
            model_name="message",
            name="is_pin",
        ),
        migrations.AddField(
            model_name="chat",
            name="is_watched",
            field=models.BooleanField(default=False),
        ),
    ]
