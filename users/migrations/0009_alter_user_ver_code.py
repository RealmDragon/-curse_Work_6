# Generated by Django 4.2.2 on 2024-09-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_user_ver_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="ver_code",
            field=models.CharField(
                default="870982689842", max_length=15, verbose_name="код из письма"
            ),
        ),
    ]
