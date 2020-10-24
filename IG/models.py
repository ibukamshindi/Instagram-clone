from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from friendship.models import Friend,Follow,Block

# Create your models here.
class Profile(models.Model):
      profile_photo=models.ImageField(upload_to='profiles/',null=True)
      user_bio=models.TextField()
      user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
      last_update = models.DateTimeField(auto_now_add=True, null=True)

class Meta:
      ordering =['-last_update']      


      def __str__(self):
         return self.user.username

      def save_profile(self):
          self.save()
      
      def delete_profile(self):
          self.delete()


class Image(models.Model):
      image=models.ImageField(upload_to='photos',null=True)
      image_name=models.CharField(max_length =30,null=True)
      image_caption=models.TextField()
      likes = models.IntegerField(default=0)
      date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
      user = models.ForeignKey(User, null=True)
      profile=models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

class Meta:
      ordering = ['-date_uploaded']      

      def save_image(self):
          self.save()

      def delete_image(self):
          self.delete()

      @classmethod
      def search_by_user(cls, search_term):
          images = cls.objects.filter(image_caption__icontains=search_term)
          return images

      @classmethod
      def get_image_by_id(cls, image_id):
          images = cls.objects.get(id=image_id)
          return images
    

class Comment(models.Model):
    comment=models.TextField()
    image=models.ForeignKey(Image,null=True,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    time_comment = models.DateTimeField(auto_now_add=True, null=True)

class Meta:
    ordering = ['-time_comment']    

    def __str__(self):
        return str(self.comment)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments


# class Likes(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     image=models.ForeignKey(Image,on_delete=models.CASCADE)

    