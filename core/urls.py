from django.urls import path, include
from .views import (
  
    checkout,
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart
)
app_name='core'

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
     path('checkout/', checkout,name='checkout'),
     path('products/<slug>/ ', ItemDetailView.as_view(),name='product'),
     path('add-to-cart/<slug>/',add_to_cart,name='add_to_cart'),
     path('remove-from-cart/<slug>/',remove_from_cart,name='remove_from_cart')
]