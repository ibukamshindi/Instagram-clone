from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
      profile_photo=ImageField(blank=True)
      bio=models.TextField()
      user=models.OneToOneField(User,on_delete=models.CASCADE)

class Image(models.Model):
    image=ImageField(manual_crop="1080x800",null=True)
    image_name=models.CharField(max_length =30,null=True)
    image_caption=models.TextField()
    profile=models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    

class Comment(models.Model):
    comment=models.TextField()
    image=models.ForeignKey(Image,null=True,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)


class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)

    