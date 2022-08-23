# Generated by Django 4.0.7 on 2022-08-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0005_alter_student_date_of_birth_and_more'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='attachments',
            field=models.FileField(blank=True, upload_to='attachments'),
        ),
        migrations.AddField(
            model_name='post',
            name='saves',
            field=models.ManyToManyField(blank=True, related_name='post_saves', to='user_mgmt.baseuser'),
        ),
        migrations.AddField(
            model_name='post',
            name='type_of_post',
            field=models.CharField(choices=[('TXT', 'text'), ('IMG', 'Image'), ('VID', 'Video'), ('DOC', 'Document')], default='TXT', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to='user_mgmt.baseuser'),
        ),
        migrations.AlterField(
            model_name='post',
            name='shares',
            field=models.ManyToManyField(blank=True, related_name='post_shares', to='user_mgmt.baseuser'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]