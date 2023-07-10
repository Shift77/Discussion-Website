from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
# Create your views here.

def category_detail(request, id):
    
    category = get_object_or_404(models.Category, id=id)
    
    all_posts = category.post_category.all()
    
    
    
    context = {
        'category': category,
        
    }
    
    return render(request, 'discussion_app/category.html', context)