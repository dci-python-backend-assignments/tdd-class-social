# Generated by Django 4.0.6 on 2022-07-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_commented_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_date',
            field=models.DateField(),
        ),
    ]
