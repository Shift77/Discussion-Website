from django.shortcuts import render
from discussion_app import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard_detail(request, id):
    posts = models.Post.objects.all().filter(author=request.user)
    
    context = {
        'posts':posts
    }
    
    return render(request, 'dashboard_app/dashboard.html', context)