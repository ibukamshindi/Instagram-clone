from django.test import TestCase

# Create your tests here.
from .models import Image, Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
          self.user = User.objects.create_user("testuser", "secret")
          self.profile_test = Profile(profile_photo='this is me',
                                            bio="this is a test bio",
                                            owner=self.user)
          self.profile_test.save()

    def test_instance_true(self):
          self.profile_test.save()
          self.assertTrue(isinstance(self.profile_test, Profile))


    # def setUp(self):
    #     user=User(username='pato')
    #     self.profile=Profile(profile_photo='this is me',bio='execeptional',user=user)

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.profile,Profile))

    # def test_save_method(self):
    #     self.profile.save_profile()
    #     profiles=Profile.objects.all()
    #     self.assertTrue(len(profiles)>0)

    # def test_delete_method(self):
    #     self.profile.save_profile()
    #     profiles = Profile.objects.all()
    #     self.profile.delete_profile()
    #     profiles = Profile.objects.all()
    #     self.assertTrue(len(profiles)==0)

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

class CommentTestClass(TestCase):
  
    """Test class for Comment Model"""

    def setUp(self):
        self.new_user = User.objects.create_user("testuser", "secret")

        self.new_profile = Profile(profile_phot='this is me',
                                     bio="this is a test bio",
                                     owner=self.new_user)
        self.new_profile.save()

        self.new_image = Image(pic='https://ucarecdn.com/620ac26e-19f7-4c0a-86d1-2b4e4b195fa8/-/crop/610x452/15,0/-/preview/',
                               caption="this is a test image", profile='',profile_details=self.new_user)
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, comment_owner=self.new_profile, comment="this is a comment on a post")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()