from django.urls import path
from . import views
from .views import contact_view


urlpatterns = [
     
    path('home/', views.home, name='home'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('product-list/', views.product_list, name='product_list'),
    path('contact/', views.contact_us, name='contact_us'),
    path('myaccount/', views.my_account, name='my_account'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('myorders/', views.view_orders, name='view_orders'),
    path('about-us/', views.about_us, name='about_us'),
    path('signup/', views.signup_view, name='signup'),
    path('order/<int:product_id>/', views.place_order, name='place_order'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('online-payment/', views.online_payment, name='online_payment'),
    path('confirm-order/', views.confirm_order, name='confirm_order'),
    path('process-order/', views.process_order, name='process_order'),
]
