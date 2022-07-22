from django.db import models

# Create your models here.

# QUESTION: how to related_name????????????????????????????????????????????????????????????????
# QUESTION: how to filter for different fields of courses? Like current, completed, active, old
# QUESTION: two models in many to many field, like Union[students, teachers]
# QUESTION: List of phone numbers, how to JSONFIELD
# QUESTION: country codes for phone numbers

class BaseUser(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()
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


class Person(BaseUser):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [('U', 'Unicorn'),
                      ('F', 'Female'),
                      ('M', 'Male'),
                      ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Unicorn')
    # country codes???
    phone_number = models.IntegerField()


class Course(models.Model):
    pass


class ResearchProject(models.Model):
    pass


class Institution(BaseUser):
    name = models.CharField(max_length=300)
    phone_numbers = models.IntegerField()
    associates = models.ManyToManyField(BaseUser, symmetrical=False, related_name='institutions', blank=True)
    association_requests = models.ManyToManyField(BaseUser, symmetrical=False, related_name='institutions', blank=True)
    head_of_organization = models.CharField(max_length=300)
    research_institution = models.BooleanField(default=False, null=True, blank=True)
    education_institution = models.BooleanField(default=False, null=True, blank=True)
    research_projects = models.ManyToManyField(ResearchProject, symmetrical=False, related_name='institutions', blank=True)
    active_courses = models.ManyToManyField(Course, symmetrical=False, related_name='institutions', blank=True)
    inactive_courses = models.ManyToManyField(Course, symmetrical=False, related_name='institutions', blank=True)
    offers = models.ManyToManyField(Course, symmetrical=False, related_name='institutions', blank=True)


# class Student(Person):
#     current_courses = models.ManyToManyField(Course, symmetrical=False, related_name='students', null=True, blank=True)
#     completed_courses = models.ManyToManyField(Course, symmetrical=False, related_name='students', null=True, blank=True)
#     institution = models.ManyToManyField(Institution, symmetrical=False, related_name='students', null=True, blank=True)
#     interests = models.CharField(max_length=200, null=True, blank=True)
#
#
# class Teacher(Person):
#     courses_in_progress = models.ManyToManyField(Course, symmetrical=False, related_name='teacher', null=True, blank=True)
#     old_courses = models.ManyToManyField(Course, symmetrical=False, related_name='teacher', null=True, blank=True)
#     future_courses = models.ManyToManyField(Course, symmetrical=False, related_name='teacher', null=True, blank=True)
#     institution = models.ManyToManyField(Institution, symmetrical=False, related_name='teacher', null=True, blank=True)
#     interests = models.CharField(max_length=200, null=True, blank=True)