from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from systemservices.client.forms import ClientModelForm
from systemservices.client.models import Client


def list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})


def new(request):
    if request.method == 'POST':
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered client.')
        else:
            messages.error(request, 'Error registered client.')
    return render(request, 'client/client_new.html', {'form': ClientModelForm})


def detail(request, pk):
    form = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientModelForm(request.POST, instance=form)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Successfully updated client.')
        else:
            messages.error(request, 'Error updated client.')
    form = ClientModelForm(instance=form)
    return render(request, 'client/client_detail.html', {'form': form})
