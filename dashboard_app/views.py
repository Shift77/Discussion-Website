from django.shortcuts import render
from discussion_app import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard_detail(request, id):
    posts = models.Post.objects.all().filter(author=request.user)
    
    saved_posts = request.user.userprofile.saved_posts.all()
    
    context = {
        'posts':posts,
        'saved_posts':saved_posts
    }
    
    return render(request, 'dashboard_app/dashboard.html', context)