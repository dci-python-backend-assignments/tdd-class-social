# Generated by Django 4.0.6 on 2022-07-21 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_comment_commented_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 21, 18, 13, 54, 241119)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(),
        ),
    ]