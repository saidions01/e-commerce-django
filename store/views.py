
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, Product, Feedback, Category, Order
from store import views
import random
from .forms import ContactForm 
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.contrib import messages
from .forms import ContactForm
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
@login_required
def my_account(request):
    return render(request, 'myaccount.html')
@login_required
def wishlist_view(request):
    wishlisted_items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist.html', {'wishlisted_items': wishlisted_items})
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return JsonResponse({'status': 'added'})

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')
  

@login_required
def view_orders(request):
    return render(request, 'view_orders.html')

def about_us(request):
    return render(request, 'about_us.html')


def login_view(request):
    return render(request, 'login.html')


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
            login(request, user)
            return redirect('/login')  # You might want to redirect to home or dashboard instead
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def logout_view(request):
    return render(request, 'logout.html')
@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Order.objects.create(
        user=request.user,
        product=product,
        status='Pending'
    )

    return redirect('view_orders')



@login_required
def view_orders(request):
    current_user = request.user
    user_orders = Order.objects.filter(user=current_user).order_by('-date_ordered')
    return render(request, 'view_orders.html', {'orders': user_orders})
@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'Pending':
        order.delete()
        messages.success(request, f"Order #{order.id} has been canceled.")
    else:
        messages.warning(request, "Only pending orders can be canceled.")

    return redirect('view_orders')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('edit_profile')

    return render(request, 'edit_profile.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_us')  # Redirect after successful submission
        else:
            messages.error(request, "There was an error. Please try again.")  # This will now be triggered if form is not valid
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
