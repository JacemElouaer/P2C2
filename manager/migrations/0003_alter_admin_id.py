# Generated by Django 4.0.2 on 2022-03-15 23:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('76b05581-f96f-4df0-b216-d1678e4a3e81'), primary_key=True, serialize=False),
        ),
    ]
