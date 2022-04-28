from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'core/index.html', context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {"form": form})


def product_desc(request, pk):
    products = Product.objects.get(pk=pk)
    context = {"products": products}
    return render(request, 'core/product_desc.html', context)
