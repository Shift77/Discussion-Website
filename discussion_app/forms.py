from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['likes']
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['content']
        
        
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'w-full rounded-xl border-2 border-black text-lg p-4 mb-2',
        'placeholder':'Leave a message . . . '
    }))