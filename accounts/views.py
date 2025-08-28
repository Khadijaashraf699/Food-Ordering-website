from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user= authenticate(request, username=username, password=password)
    
        if user is not None:
           login(request, user)
           return redirect('home')
        else:
           return render(request, 'login.html', {'error','Invalid your username and password'})

            
    return render(request, 'login.html')     

