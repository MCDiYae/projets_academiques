from django.shortcuts import render, HttpResponse, redirect
from .models import Client
from Commande.models import Commande
from .forms import ClientForm


# Create your views here.
def list_client(request):
    clients = Client.objects.all()
    commandes = Commande.objects.all()
    context = {'clients': clients,'commandes': commandes}
    return render(request, 'client/list_client.html',context)


def ajouter_client(request):
    print("apel au ajouter")
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_client')
    else:
        form = ClientForm()
        context = {'form': form}
    return render(request, 'client/ajouter_client.html',context)
