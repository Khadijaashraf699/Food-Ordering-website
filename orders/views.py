from django.shortcuts import render
from orders.models import Category

# Create your views here.
def home(request):
    category = Category.objects.all()
    context={
        'category': category
    }
    return render(request, 'index.html', context)
