

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Product
from store import views
import random
from .forms import ContactForm 
from .models import Feedback
from .models import Category
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def home(request):
    all_products = list(Product.objects.all())
    random_products = random.sample(all_products, min(len(all_products), 8))
    feedbacks = Feedback.objects.all() 
    categories = Category.objects.all()[:3]
 

    return render(request, 'home.html', {
        'random_products': random_products,
        'feedbacks': feedbacks,
        'categories': categories
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def my_account(request):
    return render(request, 'myaccount.html')

def wishlist_view(request):
    wishlisted_items = Wishlist.objects.select_related('product')  
   
    return render(request, 'wishlist.html', {'wishlisted_items': wishlisted_items})


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create( product=product)
    return redirect('wishlist')

def view_orders(request):
    return render(request, 'view_orders.html')

def about_us(request):
    return render(request, 'about_us.html')



def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter( product=product).delete()
    return redirect('wishlist')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
         
            return render(request, 'contact.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def feedback_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in directly after signing up
            return redirect('/login')  # redirect to your homepage
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
