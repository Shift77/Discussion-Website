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
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    
    title = models.CharField(max_length=300)
    
    views = models.IntegerField(default=0)
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def involved_users(self):
        all_messages = self.message_post.all()
        
        all_users = [self.author]
        
        for message in all_messages:
            if message.author not in all_users:
                all_users.append(message.author)
                
        return [all_users, len(all_users)]
    
    
class Message(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='message_post')

    replies = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='message_replies')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_author')

    likes = models.ManyToManyField(User, related_name='message_likes', blank=True)
    
    content = models.TextField(max_length=1000)
    
    last_modified_date = models.DateTimeField(auto_now=True)
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
    @property
    def is_parent(self):
        if self.replies is None:
            return True
        
        return False
    
    def children(self):
        return Message.objects.filter(replies=self).reverse()