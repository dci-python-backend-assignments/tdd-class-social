# Generated by Django 4.0.7 on 2022-08-22 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0003_alter_student_courses_alter_student_institution_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='phone_numbers',
        ),
        migrations.AddField(
            model_name='teacher',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('U', 'Unicorn'), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='Unicorn', max_length=1),
        ),
    ]