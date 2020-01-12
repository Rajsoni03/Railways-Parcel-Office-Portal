# Generated by Django 2.2.6 on 2020-01-11 06:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20200110_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('long', models.CharField(max_length=100)),
                ('total_train', models.PositiveIntegerField()),
                ('train_no', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='train',
            name='train_from_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 11, 6, 40, 46, 112503, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_to_time',
            field=models.TimeField(default=datetime.datetime(2020, 1, 11, 6, 40, 46, 112503, tzinfo=utc)),
        ),
    ]