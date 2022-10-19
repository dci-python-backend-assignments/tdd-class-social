from django.db import models

GENDER_CHOICES = [('U', 'Unicorn'),
                  ('F', 'Female'),
                  ('M', 'Male'),
                  ('O', 'Other')]


class BaseUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    connections = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)

    def __str__(self):
        return self.username


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, default=None)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return f"{self.name}-{self.id}"


class Institution(BaseUser):
    name = models.CharField(max_length=300)
    associates = models.ManyToManyField(BaseUser, symmetrical=False, related_name='institutions', blank=True)
    head_of_organization = models.CharField(max_length=300)
    research_institution = models.BooleanField(default=False, null=True, blank=True)
    education_institution = models.BooleanField(default=False, null=True, blank=True)
    courses = models.ManyToManyField(Course, symmetrical=False, related_name='courses', null=True, blank=True)


class Student(BaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    courses = models.ManyToManyField(Course, symmetrical=False, related_name='students', null=True, blank=True)
    institution = models.ManyToManyField(Institution, symmetrical=False, related_name='students', null=True, blank=True)
    interests = models.TextField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Unicorn')

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class CourseParticipant(models.Model):
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_name', on_delete=models.CASCADE)
    completed = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'course_participant'

    def __str__(self):
        return self.course, self.student


class Teacher(BaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    courses = models.ManyToManyField(Course, symmetrical=False, related_name='teacher', null=True, blank=True)
    institution = models.ManyToManyField(Institution, symmetrical=False, related_name='teacher', null=True, blank=True)
    interests = models.TextField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Unicorn')


class MyFile(models.Model):
    file = models.FileField(blank=False, null=False, upload_to='images/')
    description = models.CharField(null=True, max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'MyFiles'
# https://www.youtube.com/watch?v=UKE5yQAmg0k
# https://stackoverflow.com/questions/69119309/pass-row-data-from-csv-to-api-and-append-results-to-an-empty-csv-column
