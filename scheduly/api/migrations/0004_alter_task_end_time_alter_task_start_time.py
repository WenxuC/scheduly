# Generated by Django 4.1 on 2022-08-11 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_task_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
