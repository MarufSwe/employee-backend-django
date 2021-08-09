# Generated by Django 3.2.4 on 2021-08-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0004_createreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateMerchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, unique=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]