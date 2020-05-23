from django.shortcuts import render
from  .models import Item
from django.views.generic import ListView,DetailView



# Create your views here.
def products(request):
    context={
        'items':Item.objects.all()
    }
    return render (request,"product-page.html",context)
class HomeView(ListView):
    model=Item
    template_name="home-page.html"

class ItemDetailView(DetailView):
     model=Item 
     template_name="product.html "
     
def checkout(request):
    return render(request,"checkout-page.html")