from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'core/index.html')


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {"form": form})
