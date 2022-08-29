# Generated by Django 4.0.7 on 2022-08-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0006_alter_baseuser_connections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='connections',
            field=models.ManyToManyField(blank=True, null=True, to='user_mgmt.baseuser'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses', to='user_mgmt.course'),
        ),
    ]