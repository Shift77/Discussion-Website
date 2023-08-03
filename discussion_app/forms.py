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