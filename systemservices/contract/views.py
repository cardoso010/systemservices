from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from systemservices.contract.forms import ContractModelForm
from systemservices.contract.models import ContractedService


def list(request):
    hired = ContractedService.objects.all()
    return render(request, 'contract/contract_list.html', {'hired': hired})


def new(request):
    if request.method == 'POST':
        form = ContractModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered contract.')
        else:
            messages.error(request, 'Error registered client.')
    return render(request, 'contract/contract_new.html', {'form': ContractModelForm})


def detail(request, pk):
    form = get_object_or_404(ContractedService, pk=pk)
    if request.method == 'POST':
        form = ContractModelForm(request.POST, instance=form)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Successfully updated contract.')
        else:
            messages.error(request, 'Error updated contract.')
    form = ContractModelForm(instance=form)
    return render(request, 'contract/contract_detail.html', {'form': form})


def remove(request, pk):
    ContractedService.objects.get(pk=pk).delete()
    hired = ContractedService.objects.all()
    return render(request, 'contract/contract_list.html', {'hired': hired})
