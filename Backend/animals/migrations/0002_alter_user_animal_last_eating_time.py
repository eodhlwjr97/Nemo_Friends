# Generated by Django 3.2.12 on 2022-09-14 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_animal',
            name='last_eating_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 8, 2, 28, 50424)),
        ),
    ]
