
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from store.views import home





def product_list(request):
    return render(request, 'product_list.html')

def login_view(request):
    return render(request, 'registration/login.html')