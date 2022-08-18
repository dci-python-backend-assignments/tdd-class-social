from datetime import datetime
from django.db import models

# from djangotoolbox.fields import ListField

"""Some times when you try to alter some column field in the data base it causes some problem and pycharm ask you to make nullable by setting a default value.  
This could be solved by deleting all the migration (click on the migrations package in the project navigator to delete them
then delete the db.sqlite3 file then initiate the migration again"""


# todo initial simple user model just to test the post models
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# still under construction😉


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    content = models.TextField(default='')
    creation_date = models.DateField()  # DateField(default=datetime, null=True)
    creator = models.ForeignKey(User, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)  # todo check it

    # comments_on_this_post = models.ManyToManyField(User, related_name='commented_posts')
    # comments_on_this_post = ListField(null=True)
    likes_for_this_post = models.ManyToManyField(User, related_name='likes')
    shares_for_this_post = models.ManyToManyField(User, related_name='shares')
    type_of_post = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    commented_date = models.DateField()  # DateTimeField(default=datetime)

    def __str__(self):
        return f"{self.content}"  # todo try to figure out how to display the name of the commenter


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    pass


# todo initial idea still needs to be checked
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    starting_date = models.DateField()
    end_date = models.DateField()
    starting_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, null=True, blank=True, related_name='courses', on_delete=models.SET_NULL)
