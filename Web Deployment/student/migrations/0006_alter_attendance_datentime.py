# Generated by Django 4.1.1 on 2022-09-29 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_attendance_datentime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='datentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 0, 14, 11, 890701)),
        ),
    ]
