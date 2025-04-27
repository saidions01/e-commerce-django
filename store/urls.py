from django.urls import path
from . import views
from .views import contact_view


urlpatterns = [
   
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('home/', views.home, name='home'),
    path('product-list/', views.product_list, name='product_list'),
    path('contact/', contact_view, name='contact'),
    path('myaccount/', views.my_account, name='my_account'),
    path('myorders/', views.view_orders, name='view_orders'),
    path('about-us/', views.about_us, name='about_us'),
]
