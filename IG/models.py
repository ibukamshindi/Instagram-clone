from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from friendship.models import Friend,Follow,Block

# Create your models here.
class Profile(models.Model):
      profile_photo=models.ImageField(upload_to='profiles/',null=True)
      bio=models.TextField()
      owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

      def __str__(self):
         return self.user.username

      def save_profile(self):
          self.save()
      
      def delete_profile(self):
          self.delete()

class Image(models.Model):
      image=models.ImageField(upload_to='photos/',null=True)
      image_name=models.CharField(max_length =30,null=True)
      image_caption=models.TextField()
      profile=models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

      def save_image(self):
          self.save()

      def delete_image(self):
          self.delete()
    

class Comment(models.Model):
    comment=models.TextField()
    image=models.ForeignKey(Image,null=True,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)


class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)

    