# Generated by Django 4.2.7 on 2024-03-23 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("chats", "0002_rename_is_archive_message_is_watched_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="location",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.CreateModel(
            name="Archive",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("contact", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="chats.profile")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]