# Generated by Django 2.2.6 on 2020-01-10 10:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_ID', models.PositiveIntegerField()),
                ('lat', models.CharField(max_length=50)),
                ('long', models.CharField(max_length=50)),
                ('seal_status', models.BooleanField()),
                ('parcel_status', models.BooleanField()),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 10, 10, 41, 2, 929453, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': 'LiveTracking',
            },
        ),
    ]
