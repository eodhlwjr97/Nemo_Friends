# Generated by Django 3.2.12 on 2022-09-14 12:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.TextField()),
                ('feeds', models.JSONField(default=list)),
                ('characteristics', models.JSONField(default=list)),
                ('commands', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='User_Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('exp', models.IntegerField(default=0)),
                ('is_located', models.BooleanField(default=False)),
                ('color_id', models.IntegerField(default=0)),
                ('talking_cnt', models.IntegerField(default=0)),
                ('playing_cnt', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_eating_time', models.DateTimeField(default=datetime.datetime(2022, 9, 14, 8, 2, 5, 809735))),
                ('level', models.IntegerField(default=0)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
