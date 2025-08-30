from django.shortcuts import redirect, render
from orders.models import Category
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already exists'})
        
        
        user = User.objects.create_user(
            first_name=first_name, 
            email=email, 
            username=username, 
            password=password 
            )
        if user is not None:
            login(request, user)
            context={
                'message':'your account has been registered'
            }
            return render(request, 'index.html', context)
    else:
        return render(request, 'accounts/register.html')
    

    
def home(request):
    category = Category.objects.all()
    context={
        'category': category
    }
    return render(request, 'index.html', context)


