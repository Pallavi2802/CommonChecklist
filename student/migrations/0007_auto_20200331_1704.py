# Generated by Django 2.2.11 on 2020-03-31 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20200331_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='act',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='boards',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='sat',
        ),
    ]
