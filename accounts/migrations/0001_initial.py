# Generated by Django 3.1.4 on 2020-12-20 19:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreAdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StoreAdmin_slug', models.SlugField(blank=True, null=True)),
                ('StoreAdmin_image', models.ImageField(blank=True, null=True, upload_to='profile_img')),
                ('StoreAdmin_address', models.CharField(max_length=100)),
                ('StoreAdmin_join_date', models.DateTimeField(default=datetime.datetime.now)),
                ('StoreAdmin_country', django_countries.fields.CountryField(default='Jordan', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_slug', models.SlugField(blank=True, null=True)),
                ('Customer_image', models.ImageField(blank=True, null=True, upload_to='profile_img')),
                ('Customer_address', models.CharField(max_length=100)),
                ('Customer_join_date', models.DateTimeField(default=datetime.datetime.now)),
                ('Customer_country', django_countries.fields.CountryField(default='Jordan', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
