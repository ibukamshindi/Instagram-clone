from django.conf.urls import url
from .import views

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'accounts/profile/',views.profile, name='profile'),
  url(r'^showprofile/',views.display_profile, name='showprofile'),
]