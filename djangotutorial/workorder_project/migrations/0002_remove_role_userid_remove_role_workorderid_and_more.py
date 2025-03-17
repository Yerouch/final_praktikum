# Generated by Django 5.1.6 on 2025-03-16 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workorder_project", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="role",
            name="userid",
        ),
        migrations.RemoveField(
            model_name="role",
            name="workorderid",
        ),
        migrations.RemoveField(
            model_name="user",
            name="notifications",
        ),
        migrations.AddField(
            model_name="notification",
            name="role",
            field=models.ManyToManyField(
                related_name="role", to="workorder_project.role"
            ),
        ),
        migrations.AddField(
            model_name="role",
            name="users",
            field=models.ManyToManyField(
                related_name="users", to="workorder_project.user"
            ),
        ),
        migrations.AddField(
            model_name="workorder",
            name="responsible",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="workorder_project.user",
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="notification",
            name="workorder",
        ),
        migrations.AddField(
            model_name="notification",
            name="workorder",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="workorder_project.workorder",
            ),
            preserve_default=False,
        ),
    ]
