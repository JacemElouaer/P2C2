# Generated by Django 3.2.7 on 2022-03-16 08:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('07f3e1de-9bc4-4398-a9eb-3fd74dbcb653'), primary_key=True, serialize=False),
        ),
    ]