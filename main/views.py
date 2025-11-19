from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, 'main/index.html')

def products_list(request):
    items = Product.objects.all()  # Get all products from DB
    return render(request, 'main/products.html', {'products': items})

def product_detail(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'main/detail.html', {'product': item})

