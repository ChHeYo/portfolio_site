# Generated by Django 2.0.2 on 2018-02-18 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('show_portfolio', '0010_auto_20180218_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 19, 44, 17, 226751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 19, 44, 17, 226751, tzinfo=utc)),
        ),
    ]
