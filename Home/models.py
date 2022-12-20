from django.contrib.auth.models import User
from django.db import models

from Userapp.models import Account


class Blog(models.Model):
    file = models.FileField()
    title = models.TextField()
    aderes = models.CharField(max_length=25)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")


class Servi(models.Model):
    fullname = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    about_me = models.CharField(max_length=200)
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    images = models.FileField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)

class Region(models.Model):
    name = models.CharField(max_length=25)
    brief_information = models.TextField()
    file = models.FileField()


class Popular_dic(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=25)


