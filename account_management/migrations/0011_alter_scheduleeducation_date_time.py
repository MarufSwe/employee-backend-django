# Generated by Django 3.2.4 on 2021-08-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0010_alter_scheduleeducation_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleeducation',
            name='date_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
