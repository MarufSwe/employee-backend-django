# Generated by Django 3.2.4 on 2021-08-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0006_alter_createmerchandise_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmerchandise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Product Image'),
        ),
    ]