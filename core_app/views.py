from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from discussion_app.models import Post, Category
# Create your views here.

def index(request):
    categories = Category.objects.all()
    
    print(categories[0].last_activity)
    
    context = {
        'categories': categories,
       
    }
    
    return render(request, 'core_app/index.html', context)

def signup(request):
    
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        profile_form = forms.ProfileForm(request.POST, request.FILES)
        
         #NOTE: this is a test
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            profile = profile_form.save(commit=False)
           
            profile.user = user
            
            profile.save()
            
            return redirect('/login/')
    
    
    else:
        form = forms.SignupForm
        profile_form = forms.ProfileForm
        
    context = {
        'form': form,
        'profile_form': profile_form
    }
        
    return render(request, 'core_app/signup.html', context)