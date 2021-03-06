# Generated by Django 2.0.2 on 2018-08-10 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_auto_20180810_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='v_views',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读次数'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='v_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 9, 9, 30, 159299, tzinfo=utc), verbose_name='最后更新时间'),
        ),
    ]
