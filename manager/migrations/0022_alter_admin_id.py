# Generated by Django 3.2.7 on 2022-03-16 09:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0021_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('147c42c5-6019-40dd-88e3-8fd4126e2831'), primary_key=True, serialize=False),
        ),
    ]
