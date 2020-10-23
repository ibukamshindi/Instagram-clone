from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image,Profile,Comment,Follow,Likes
from .forms import ProfileForm,ImageForm,CommentForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'home.html')

@login_required(login_url='/account/login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/accounts/login')
def display_profile(request,id):
    seekuser=User.objects.filter(id=id).first()
    profile=seekuser.profile
    profile_details=profile.get_by_id(id)
    images=Image.get_profile_images(id)

    usersss=User.objects.get(id=id)
    follower=len(Follow.objects.followers(usersss))
    following=len(Follow.objects.following(usersss))
    people=User.objects.all()
    pip_following=Follow.objects.following(request.user)

    return render(request,'profile.html',locals())


