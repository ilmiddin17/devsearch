from distutils.command.upload import upload
from turtle import up
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.dispatch import receiver
from django.urls import translate_url
# Create your models here.
class Tag(models.Model):
    text=models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.text

class Project(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title=models.CharField(max_length=120)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='media/')
    tags=models.ManyToManyField(Tag, null=True, blank=True)
    source_code=models.CharField(null=True, blank=True, max_length=400)
    demo_link=models.CharField(null=True, blank=True, max_length=200)
    vote_count=models.IntegerField(null=True, blank=True)
    vote_ratio=models.IntegerField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_CHOICES=(
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    body=models.TextField(null=True, blank=True)
    value=models.CharField(max_length=20, choices=VOTE_CHOICES)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.value
    

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    headline=models.CharField(max_length=120, null=True, blank=True)
    bio=models.CharField(max_length=120, null=True, blank=True)
    location=models.CharField(max_length=300, null=True, blank=True)
    profile_image=models.ImageField(upload_to='media/profiles/', null=True, blank=True)
    social_github=models.URLField(verbose_name='Github', null=True, blank=True, max_length=300)
    social_linkedin=models.URLField(verbose_name='LinkedIn', null=True, blank=True, max_length=300)
    social_twitter=models.URLField(verbose_name='Twitter', null=True, blank=True, max_length=300)
    social_youtube=models.URLField(verbose_name='YouTube', null=True, blank=True, max_length=300)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username

class Skill(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    sender=models.OneToOneField(User, on_delete=models.CASCADE, related_name='sender')
    recipient=models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipient')
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200, blank=True, null=True)
    body=models.TextField()
    is_read=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.sender.username
