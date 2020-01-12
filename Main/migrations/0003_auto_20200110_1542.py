# Generated by Django 2.2.6 on 2020-01-10 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20200110_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='tarin_days',
            field=models.CharField(default=datetime.datetime(2020, 1, 10, 10, 12, 44, 858571, tzinfo=utc), max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='train_from_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 10, 10, 11, 47, 324498, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='train',
            name='train_to_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 10, 10, 11, 47, 324498, tzinfo=utc)),
        ),
    ]