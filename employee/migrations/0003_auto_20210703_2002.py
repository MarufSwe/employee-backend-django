# Generated by Django 3.2.4 on 2021-07-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_availableinventory_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availableinventory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]