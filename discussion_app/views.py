from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
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
    
    post_saved = request.user.userprofile.saved_posts.filter(id=id).exists()
    
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
        'is_liked':is_liked,
        'post_saved':post_saved
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
        
    return HttpResponseRedirect(reverse('discussion_app:post_detail', args=(id,)))

@login_required
def comment_like(request, id):
    comment = get_object_or_404(models.Message, id=id)
    
    is_liked = comment.likes.filter(id=request.user.id).exists()
    
    if is_liked:
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        
    post_id = request.POST.get('comment_like')    
    
    return HttpResponseRedirect(reverse('discussion_app:post_detail', args=(post_id,)))

@login_required
def post_save(request, id):
    post = get_object_or_404(models.Post, id=id)
    
    saved_posts = request.user.userprofile.saved_posts
    
    is_saved = saved_posts.filter(id=id).exists()
    
    if is_saved:
        saved_posts.remove(post)
        
    else:
        saved_posts.add(post)
        
    return HttpResponseRedirect(reverse('discussion_app:post_detail', args=(id,)))

@login_required
def create_post(request):    
    
    form = forms.CreatePostForm
    
    if request.method == 'POST':
        form = forms.CreatePostForm(request.POST)        
        if form.is_valid():
            
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            
            return HttpResponseRedirect(reverse('discussion_app:category_detail', args=str(f.category.id)))
        else:
            print("could'nt validate")
    
    context = {
        'form':form
    } 
    
    return render(request, 'discussion_app/create_post.html', context)

@login_required
def delete_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    
    category_id = post.category.pk

    post.delete()
        
    return HttpResponseRedirect(reverse('discussion_app:category_detail', args=str(category_id)))


@login_required
def edit_post(request, id):
    post = get_object_or_404(models.Post, id=id)
    
    if request.method == 'POST':
        
        form = forms.CreatePostForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            
            return redirect(reverse('discussion_app:post_detail', args=(id,)))

        
        
    
    form = forms.CreatePostForm(instance=post)
   
    edit = True
   
    context = {
        'form':form,
        'edit':edit
    }
    
    return render(request, 'discussion_app/create_post.html', context)

def search_posts(request):
    search_query = request.GET.get('search')
    print(search_query)
    
    if search_query:
        posts = models.Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        
        context = {
            'posts':posts,
            'search_query':search_query
        }
        return render(request, 'discussion_app/search.html', context)
    else:
        return redirect(reverse('core_app:index'))