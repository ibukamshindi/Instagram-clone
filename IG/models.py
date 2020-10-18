from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
      profile_photo=models.ImageField(manual_crop="",blank=True)
      bio=models.TextField()
      user=models.OneToOneField(User,on_delete=models.CASCADE)

class Image(models.Model):
    image=models.ImageField(manual_crop='1080x800',null=True)
    image_name=models.models.CharField(max_length =30,null=True)
    image_caption=models.TextField()
    profile=models.ForeignKey(Profile,null=True)
    

class Comment(models.Model):
    comment=models.CharField()
    image=models.ForeignKey(Image,null=True)
    user=models.ForeignKey(User,null=True)


class Likes(models.Model):
    user=models.ForeignKey(User)
    image=models.ForeignKey(Image)

    