from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Category)

@admin.register(models.Post)
class PostModel(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'creation_date',
        'last_modified_date' 
    )
    
@admin.register(models.Message)
class MessageModel(admin.ModelAdmin):
    list_display = [
        'content',
        'author',
        'creation_date',
        'last_modified_date' 
    ]