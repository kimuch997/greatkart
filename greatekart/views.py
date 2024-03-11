from django.shortcuts import render
from store.models import Product

def home(request):
    # Retrieve all available products
    products = Product.objects.all().filter(is_avaliable = True)

    # Prepare context data to be passed to the template
    context = {
        'products':products
    }
    # Render the 'home.html' template with the context data
    return render(request,'home.html',context) 