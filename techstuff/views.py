from django.shortcuts import render
from django.shortcuts import render



# Create your views here.

def git(request):

    return render(request, 'techstuff/gitlist.html', {'page_title': 'Git Command Cheatsheet'})
