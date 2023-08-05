from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['likes']
        
class MessageForm(forms.ModelForm):
    
    submit_message = forms.BooleanField(widget=forms.HiddenInput(), initial=True) 
    
    class Meta:
        model = models.Message
        fields = ['content']
        
        
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'w-full rounded-xl border-2 border-black text-lg p-4 mb-2',
        'placeholder':'Leave a message . . . '
    }))
    
class ReplyForm(forms.ModelForm):
    
    submit_reply = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    
    class Meta:
        model = models.Message
        fields = ['content']
        
        
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'h-40 w-full rounded-xl border-2 border-black text-lg p-4 mb-2',
        'placeholder':'Leave a reply . . . '
    }))
    
class CreatePostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # CATEGORY_CHOICES = [(c.id, c.name) for c in models.Category.objects.all()]
    
        # self.fields['category'].choices = CATEGORY_CHOICES
    
    class Meta:
        model = models.Post
        fields = ['category', 'title', 'content']
        
    
    category = forms.ModelChoiceField(label='Category',initial=models.Category.objects.all()[0] ,queryset=models.Category.objects.all() , required=True, widget=forms.Select(attrs={
        'class':'p-4 border text-lg rounded-xl w-full border-teal-400'
    }))
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your title . . .',
        'class':'p-4 text-lg rounded-xl border-teal-400 border w-full'
    }))
    
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Your content . . .',
        'class':'p-4 text-lg rounded-xl border-teal-400 border w-full'
    }))