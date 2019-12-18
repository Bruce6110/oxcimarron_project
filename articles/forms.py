from django import forms
from django.utils.translation import gettext as _  #for translation
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body','image']
     
    title=forms.CharField()
    image=forms.ImageField()
    
    body=forms.CharField(widget=forms.Textarea(attrs={'rows':9,'cols':74,'class':'special'}))
       #overrides default of TextInput
    

class CommentForm(forms.ModelForm):#by default, django generates a form dynamically but we can specify our own fields as shown
    class Meta:
        model= Comment
        fields = ('author','comment') 
       

