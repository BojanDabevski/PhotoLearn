from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserCustom(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=1000,null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    files = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

"""
class Lesson(models.Model):
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    content = models.TextField()
    video = models.FileField(upload_to='videos_uploaded', null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
"""
