from django.shortcuts import render
from systemservices.core.forms import ClientModelForm, ServiceModelForm


def home(request):
    return render(request, 'index.html')


def client_new(request):
    if request.method == 'POST':
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
    return render(request, 'client/new.html', {'form': ClientModelForm})


def service_new(request):
    if request.method == 'POST':
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
    return render(request, 'service/new.html', {'form': ServiceModelForm})