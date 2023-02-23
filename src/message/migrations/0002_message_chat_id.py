# Generated by Django 4.1.7 on 2023-02-22 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
        ("message", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="chat_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="chat_id",
                to="chat.chat",
            ),
        ),
    ]
