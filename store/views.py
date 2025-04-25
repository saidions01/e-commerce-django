
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Product
from store import views
import random

def home(request):
    all_products = list(Product.objects.all())
    random_products = random.sample(all_products, min(len(all_products), 8))
    return render(request, 'home.html', {'random_products': random_products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})




def wishlist_view(request):
    wishlisted_items = Wishlist.objects.select_related('product')  # no user filter
   
    return render(request, 'wishlist.html', {'wishlisted_items': wishlisted_items})


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')
