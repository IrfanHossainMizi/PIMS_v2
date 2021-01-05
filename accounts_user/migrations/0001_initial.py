# Generated by Django 3.1.3 on 2021-01-05 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SodeshEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SodeshOwnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('plot_no', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('paid_ammount', models.CharField(max_length=20)),
                ('Total_ammount', models.CharField(max_length=20)),
                ('update_date', models.DateField(default=datetime.datetime.now)),
                ('first_installment', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SornaliEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SornaliOwnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('plot_no', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('paid_ammount', models.CharField(max_length=20)),
                ('Total_ammount', models.CharField(max_length=20)),
                ('update_date', models.DateField(default=datetime.datetime.now)),
                ('first_installment', models.DateField()),
            ],
        ),
    ]
