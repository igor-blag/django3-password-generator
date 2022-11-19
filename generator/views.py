import random
import string

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
    
def about(request):
    return render(request, 'generator/about.html')

def password(request):
    length = 10
    thepassword = ''
    characters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('special'):
        characters.extend(string.punctuation)
    if request.GET.get('numbers'):
        characters.extend([str(x) for x in range(10)])

    length = int(request.GET.get('length', 12))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
