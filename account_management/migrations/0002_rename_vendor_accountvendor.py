# Generated by Django 3.2.4 on 2021-08-06 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendor',
            new_name='AccountVendor',
        ),
    ]