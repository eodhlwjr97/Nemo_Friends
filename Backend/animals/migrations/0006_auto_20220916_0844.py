# Generated by Django 3.2.12 on 2022-09-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_alter_user_animal_last_eating_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_animal',
            name='grade',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user_animal',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user_animal',
            name='playing_cnt',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='user_animal',
            name='talking_cnt',
            field=models.IntegerField(default=3),
        ),
    ]
