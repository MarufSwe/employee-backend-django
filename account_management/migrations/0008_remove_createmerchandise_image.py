# Generated by Django 3.2.4 on 2021-08-09 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0007_alter_createmerchandise_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createmerchandise',
            name='image',
        ),
    ]