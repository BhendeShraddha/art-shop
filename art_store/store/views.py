# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product  # Assuming you have a Product model

# View for the index page
def index(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'store/index.html', {'products': products})

# View for the product detail page
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    return render(request, 'store/product_detail.html', {'product': product})

