# Generated by Django 3.2.7 on 2022-03-16 02:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fc108ed1-9553-4df3-b92b-861930d8cf91'), primary_key=True, serialize=False),
        ),
    ]