# Generated by Django 2.2.6 on 2020-01-16 20:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nitification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 16, 20, 3, 58, 730529, tzinfo=utc)),
        ),
    ]
