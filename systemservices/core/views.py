from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from systemservices.core.forms import ClientModelForm, ServiceModelForm


def home(request):
    return render(request, 'index.html')


def client_new(request):
    form = ClientModelForm()
    if request.method == 'POST':
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered client.')
        else:
            messages.error(request, 'Error registered client.')
    return render(request, 'client/new.html', {'form': form})


def service_new(request):
    form = ServiceModelForm()
    if request.method == 'POST':
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered service.')
        else:
            messages.error(request, 'Error registered service.')
    return render(request, 'service/new.html', {'form': form})