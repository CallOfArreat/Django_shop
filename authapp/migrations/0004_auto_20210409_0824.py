# Generated by Django 2.2 on 2021-04-09 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210408_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='shopuser',
            name='activation_key_expires',
        ),
    ]
