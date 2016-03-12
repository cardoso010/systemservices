from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from systemservices.services.forms import ServiceModelForm
from systemservices.services.models import Service


def list(request):
    services = Service.objects.all()
    return render(request, 'service/service_list.html', {'services': services})


def new(request):
    if request.method == 'POST':
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered service.')
        else:
            messages.error(request, 'Error registered service.')
    return render(request, 'service/service_new.html', {'form': ServiceModelForm})


def detail(request, pk):
    form = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceModelForm(request.POST, instance=form)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Successfully updated service.')
        else:
            messages.error(request, 'Error updated service.')
    form = ServiceModelForm(instance=form)
    return render(request, 'service/service_detail.html', {'form': form})


def remove(request, pk):
    Service.objects.get(pk=pk).delete()
    services = Service.objects.all()
    return render(request, 'service/service_list.html', {'services': services})
