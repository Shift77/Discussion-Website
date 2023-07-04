from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    likes = models.ManyToManyField(User, related_name='post_likes')
    
    title = models.CharField(max_length=300)
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    
    topic = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name='message_likes')
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
class Reply(models.Model):
    
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    likes = models.ManyToManyField(User, related_name='reply_likes')
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Replies'
        
    def __str__(self):
        return self.content