from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category



def store(request,category_slug=None):
    categories = None
    products = None

    # Retrieve all available products
    products = Product.objects.all().filter(is_avaliable = True)
    product_count = products.count()


    # Prepare context data to be passed to the template
    # context = {
    #     'products':products,
    #     'product_count':product_count,
    # }


    

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories, is_avaliable = True)
        product_count = products.count()
    else:    
        products = Product.objects.all().filter(is_avaliable = True)
        product_count = products.count()
    context = {  
        'products':products,
        'product_count': product_count
    }

    
    # Render the 'home.html' template with the context data
    return render(request,'store/store.html',context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug = product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product' : single_product,
    }
    return render(request,'store/product_detail.html',context)

# Create your views here.
 