from datetime import datetime

from django.urls import reverse
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
import uuid

"""
Some times when you try to alter some column field in the data base it causes some problem and pycharm ask you to
 make nullable by setting a default value.  
This could be solved by deleting all the migration (click on the migrations package in the project navigator to delete
them then delete the db.sqlite3 file then initiate the migration again
"""

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default.jpg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    creator = models.ForeignKey(User, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # number_of_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='bloglikes', blank=True)
    # number_of_shares = models.IntegerField(default=0)
    shares = models.ManyToManyField(User, related_name='blogshares', blank=True)
    # saves = models.ManyToManyField(User, related_name="blogsave", blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_shares(self):
        return self.saves.count()

    def __str__(self):
        return f"{self.creator}: {self.content}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    commented_date = models.DateTimeField(auto_now_add=True)  # DateTimeField(default=datetime)
    likes = models.ManyToManyField(User, related_name="blogcomment", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' % (self.post.title, self.name, self.id)
        # return f"{self.user} commented on {self.post.creator}'s post"  # todo try to figure out how to display the name of the commenter

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})

#
# class LikePost(models.Model):
#     post_id = models.CharField(max_length=500)
#     username = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


