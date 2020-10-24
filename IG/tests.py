from django.test import TestCase

# Create your tests here.
from .models import Image, Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        user=User(username='pato')
        self.profile=Profile(profile_photo='this is me',bio='execeptional',user=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

class ImageTestClass(TestCase):
  
    def setUp(self):
        self.image = Image(image ='imageurl', image_name='humour', image_caption='hehe')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

