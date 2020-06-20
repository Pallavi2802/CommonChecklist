from django.db import models
from django.contrib.auth.models import User
from Counselor.models import CounselorProfile
from django.utils import timezone


# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Default name", max_length=1000)
    school = models.CharField(max_length=1000)
    newmessage = models.BooleanField(default=False)
    counselor = models.ForeignKey(CounselorProfile, on_delete=models.CASCADE, null=True, related_name="students",
                                  default=None, blank=True)

    def __str__(self):
        return self.name


class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="essays")
    link = models.URLField(max_length=1000)
    name = models.CharField(max_length=500)
    date = models.DateField()


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    category = models.CharField(max_length=500)
    grades = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    hourperweek = models.IntegerField()
    weeksperyear = models.IntegerField()
    awards = models.CharField(max_length=500)
    description = models.CharField(max_length=200)


class Testing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tests")
    type = models.CharField(max_length=200)
    date = models.DateField()
    transcripts = models.FileField(upload_to='sat2/')


class Transcript(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transcripts")
    grade = models.CharField(max_length=50)
    transcripts = models.FileField(upload_to='transcripts/')


class LOR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lors")
    recommender = models.CharField(max_length=200)
    post = models.CharField(max_length=200, default='HOD')
    email = models.CharField(max_length=200, default="samyakjainbvs@gmail.com")
    lor = models.FileField(upload_to='lor/')


class Invite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invites")
    counselor_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="email")
    token = models.CharField(max_length=11)


class Notes(models.Model):
    counselor_name = models.CharField(max_length=264)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    text = models.CharField(max_length=2640)
    date = models.DateTimeField(null=True, auto_now_add=True)


class Deadline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    date = models.DateTimeField()

class College(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="college")
    name = models.CharField(max_length=500)
    order = models.CharField(max_length=3)
    date = models.DateField()
