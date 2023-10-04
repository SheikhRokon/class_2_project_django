from django.shortcuts import render,redirect
from .form import *
from django.contrib import messages

from .models import *

# Create your views here.

def index(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile
    }
    return render(request, 'new_app/index.html',context) 

def contact(request):
    if request.method == 'post':
        print('saa dakjka',request.post)
        form = Contact_f(request.post)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('/')
        else:
            form =Contact_f()
            return render(request,'userapp/contact.html') 
    
    return render(request, 'new_app/contact.html')


def projects(request):
    return render(request, 'new_app/projects.html')
def resume(request):
    return render(request, 'new_app/resume.html')

