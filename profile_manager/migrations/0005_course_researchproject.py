# Generated by Django 4.0.6 on 2022-07-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0004_alter_person_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
