
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from store import views

@login_required
def home(request):
    return render(request, '/ecommerce_platform/store/templates/home.html')

@login_required
def product_list(request):
    return render(request, 'product_list.html')

def login_view(request):
    return render(request, '/ecommerce_platform/store/templates/registration/login.html')