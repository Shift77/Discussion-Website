from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=255)
    
    logo = models.ImageField(upload_to='post_logos/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    
    title = models.CharField(max_length=300)
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    
    topic = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    replies = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name='message_likes', blank=True)
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
