# Generated by Django 3.2.4 on 2021-08-06 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0002_rename_vendor_accountvendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('no_of_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acc_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_education', to='account_management.accountvendor')),
            ],
        ),
    ]
