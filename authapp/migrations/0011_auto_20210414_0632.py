# Generated by Django 2.2 on 2021-04-14 03:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210413_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 3, 32, 4, 118607, tzinfo=utc)),
        ),
    ]
