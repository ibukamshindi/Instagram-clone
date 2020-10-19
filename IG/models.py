from django.db import models
from django.contrib.auth.models import User
from django.db import transaction

# Create your models here.
class Profile(models.Model):
      profile_photo=models.ImageField(upload_to='profiles/',null=True)
      bio=models.TextField()
      user=models.ForeignKey(User,on_delete=models.CASCADE)


      def __str__(self):
         return self.user.username

      def save_profile(self):
          self.save()
      
class Image(models.Model):
    image=models.ImageField(upload_to='photos/',null=True)
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

    