from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from Commande.models import Commande
# Create your views here.


def index(request):
    clients = Client.objects.all()

    commandes = Commande.objects.all()

    context = {'clients': clients, 'commandes': commandes}

    return render(request, 'client/list_clients.html', context)


def detail_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    context = {'client': client}
    return render(request, 'client/detail_client.html', context)


def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm()
        context = {'form': form}
        return render(request, 'client/ajouter_client.html', context)


def modifier_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm(instance=client)
    context = {'form': form}
    return render(request, 'client/modifier_client.html', context)


def supprimer_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')

    context = {'client': client}
    return render(request, 'client/supprimer_client.html', context)
