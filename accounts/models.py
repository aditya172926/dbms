from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset()

class UserProfile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    Designation = models.CharField(max_length=200, default='')
    Address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length = 15, default='')
    Date_of_birth = models.CharField(max_length=50, default='')
    Gender = models.CharField(max_length=20, default='')
    Staff_id = models.CharField(max_length=20, default='')

    navi_mumbai = UserProfileManager()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

class Department(models.Model):
    Name = models.CharField(max_length=100, default='')
    HOD = models.CharField(max_length=100, default='')
    Phone = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.Name

class Course(models.Model):
    Name = models.CharField(max_length=100, default='')
    Code = models.CharField(max_length=100, default='')
    Department = models.ForeignKey(Department, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name


class Student(models.Model):
    University_id = models.CharField(max_length=15, primary_key=True, default='TU')
    First_name = models.CharField(max_length=100, default='')
    Middle_name = models.CharField(max_length=100, default='', blank=True)
    Last_name = models.CharField(max_length=100, default='')
    Gender = models.CharField(max_length=20, default='')
    Date_of_birth = models.CharField(max_length=50, default='')
    Phone_number = models.CharField(max_length=15, default='')
    Address =  models.TextField(default='')
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    Department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.First_name

class Faculty(models.Model):
    First_name = models.CharField(max_length=100, default='')
    Middle_name = models.CharField(max_length=100, default='', blank=True)
    Last_name = models.CharField(max_length=100, default='')
    Gender = models.CharField(max_length=20, default='')
    Date_of_birth = models.CharField(max_length=50, default='')
    Phone_number = models.CharField(max_length=15, default='')
    Salary = models.IntegerField(default=0)
    Grade = models.CharField(max_length=10, default='')
    Designation = models.CharField(max_length=20, default='')
    Age = models.IntegerField(default=0)
    Course = models.ManyToManyField(Course)
    Department = models.ManyToManyField(Department)

    def __str__(self):
        return self.First_name

class Student_enroll(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.student_id

class Research_Project(models.Model):
    Faculty_id = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=100, default='')
    Area = models.CharField(max_length=100, default='')
    Duration = models.CharField(max_length=100, default='')

class Researcher(models.Model):
    Faculty_id = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    Project_id = models.ForeignKey(Research_Project, on_delete=models.CASCADE)