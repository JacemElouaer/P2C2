# Generated by Django 3.2.7 on 2022-03-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointCollection', '0003_alter_pointcollection_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointcollection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]