# Generated by Django 2.0.2 on 2018-02-18 18:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('show_portfolio', '0009_auto_20180218_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 18, 18, 52, 190488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 18, 18, 52, 190488, tzinfo=utc)),
        ),
    ]
