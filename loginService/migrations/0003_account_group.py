# Generated by Django 4.1.1 on 2022-11-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loginService", "0002_remove_account_email_account_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="group",
            field=models.CharField(default="", max_length=50),
        ),
    ]