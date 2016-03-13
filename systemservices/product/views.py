from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from systemservices.product.models import Product
from systemservices.product.forms import ProductModelForm


def list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def new(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered product.')
        else:
            messages.error(request, 'Error registered product.')
    return render(request, 'product/product_new.html', {'form': ProductModelForm})


def detail(request, pk):
    form = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=form)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Successfully updated product.')
        else:
            messages.error(request, 'Error updated product.')
    form = ProductModelForm(instance=form)
    return render(request, 'product/product_detail.html', {'form': form})


def remove(request, pk):
    Product.objects.get(pk=pk).delete()
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

