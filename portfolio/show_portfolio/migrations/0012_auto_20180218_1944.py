# Generated by Django 2.0.2 on 2018-02-18 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('show_portfolio', '0011_auto_20180218_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 19, 44, 20, 800361, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 19, 44, 20, 800361, tzinfo=utc)),
        ),
    ]
