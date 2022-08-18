from django.db import models


class BaseUser(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=False)
    address = models.CharField(max_length=300, null=True, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    connections = models.ManyToManyField('self', symmetrical=False, related_name='users', blank=True)
    ROLE_CHOICES = [('STD', 'Student'),
                    ('INS', 'Institution'),
                    ('TEC', 'Teacher'),
                    ('OTH', 'Others')]
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='Others')

