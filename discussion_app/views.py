from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models
from . import forms
# Create your views here.

def category_detail(request, id):
    
    category = get_object_or_404(models.Category, id=id)
    
    
    
    
    
    context = {
        'category': category,
        
    }
    
    return render(request, 'discussion_app/category.html', context)

def post_detail(request, id):
    
    post = get_object_or_404(models.Post, id=id)
    
    is_liked = post.likes.filter(id=request.user.id).exists()
    
    message_form = forms.MessageForm
    reply_form = forms.ReplyForm 
    
    if request.method == 'POST':
        
        if 'submit_message' in request.POST:
            message_form = forms.MessageForm(request.POST)
            
            if message_form.is_valid() and request.user.is_authenticated:
            
                message_form.instance.author = request.user
                message_form.instance.post = post
                message_form.save()
        
        if 'submit_reply' in request.POST:
            reply_form = forms.ReplyForm(request.POST)
        
            if reply_form.is_valid() and request.user.is_authenticated:
                
                reply_form.instance.author = request.user
                reply_form.instance.post = post
                
                parent_id = request.POST.get('reply_form')
                
                parent_message = get_object_or_404(models.Message, id=parent_id)
                
                reply_form.instance.replies = parent_message
                reply_form.save()
                

          
    
    post.views += 1
    post.save()
    
    context = {
        'post':post,
        'message_form':message_form,
        'reply_form':reply_form,
        'is_liked':is_liked
    }
    
    return render(request, 'discussion_app/post.html', context)

@login_required
def post_like(request, id):
    post = get_object_or_404(models.Post, id=id)
    
    is_liked = post.likes.filter(id=request.user.id).exists()
    
    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        
    return HttpResponseRedirect(reverse('discussion_app:post_detail', args=str(id)))