from django.urls import reverse
from django.db import models
from user_mgmt.models import BaseUser
import uuid

TYPE_OF_POST = [('TXT', 'text'),
                ('IMG', 'Image'),
                ('VID', 'Video'),
                ('DOC', 'Document')]


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    creator = models.ForeignKey(BaseUser, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)
    attachments = models.FileField(upload_to='attachments', blank=True)
    content = models.TextField(blank=True, null=True)
    type_of_post = models.CharField(max_length=200, choices=TYPE_OF_POST, default='TXT')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(BaseUser, related_name='post_likes', blank=True)
    shares = models.ManyToManyField(BaseUser, related_name='post_shares', blank=True)
    saves = models.ManyToManyField(BaseUser, related_name="post_saves", blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_shares(self):
        return self.shares.count()

    def total_saves(self):
        return self.saves.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(BaseUser, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    commented_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(BaseUser, related_name="comment_likes", blank=True)

    def total_comment_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user} commented on {self.post.creator}'s post"
