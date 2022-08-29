# Generated by Django 4.0.7 on 2022-08-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0007_alter_baseuser_connections_alter_institution_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='user_mgmt.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='institution',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='user_mgmt.institution'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher', to='user_mgmt.course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='institution',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher', to='user_mgmt.institution'),
        ),
    ]
