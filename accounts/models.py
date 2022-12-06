from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    email = models.EmailField(
    blank = True,
    verbose_name='email',
    max_length=255,
    unique=True,
    )
    
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)


    date_of_birth = models.DateField(blank = True,null=True )
    instagram_url = models.CharField(max_length=255,null=True, blank=True,)
    twitter_url = models.CharField(max_length=255,null=True, blank=True,)
    facebook_url = models.CharField(max_length=255,null=True, blank=True,)
    youtube_url = models.CharField(max_length=255,null=True, blank=True,)


    
