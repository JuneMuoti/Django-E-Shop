from django.urls import path, include
from .views import (
  
    checkout,
    HomeView,
    ItemDetailView
)
app_name='core'

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
     path('checkout/', checkout,name='checkout'),
     path('products/<slug>/ ', ItemDetailView.as_view(),name='product'),
]