from django.db import models
from django.contrib.auth.models import User
from discussion_app.models import Post
# Create your models here.

class UserProfile(models.Model):
    
        user = models.OneToOneField(User, blank=True, null=True,on_delete=models.CASCADE)
        
        biography = models.TextField(null=True, blank=True)
        
        avatar = models.ImageField(upload_to='user_images', null=True, blank=True)
        
        saved_posts = models.ManyToManyField(Post, blank=True)
        
        def __str__(self):
                return self.user.username
        
        @property
        def is_moderator(self):
                return self.user.groups.filter(name='Moderator').exists()        