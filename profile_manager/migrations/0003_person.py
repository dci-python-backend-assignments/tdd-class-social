# Generated by Django 4.0.6 on 2022-07-21 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0002_alter_baseuser_connections'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profile_manager.baseuser')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('U', 'Unicorn'), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='Unicorn', max_length=1)),
                ('phone_number', models.IntegerField(max_length=30)),
            ],
            bases=('profile_manager.baseuser',),
        ),
    ]
