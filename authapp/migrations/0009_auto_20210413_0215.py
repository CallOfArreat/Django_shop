# Generated by Django 2.2 on 2021-04-12 23:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210412_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 23, 15, 25, 34591, tzinfo=utc)),
        ),
    ]
