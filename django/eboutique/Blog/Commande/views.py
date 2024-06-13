from django.shortcuts import render, get_object_or_404, redirect
from .models import Commande
from .forms import CommandeForm
# Create your views here.


def index(request):

    commandes = Commande.objects.all()

    context = {'commandes': commandes}

    return render(request, 'commande/list_commandes.html', context)


def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_commandes')
    else:
        form = CommandeForm()
        context = {'form': form}
        return render(request, 'commande/ajouter_commande.html', context)


def modifier_commande(request, pk):
    commande = get_object_or_404(Commande, id=pk)
    if request.method == 'POST':
        form = CommandeForm(request.POST, request.FILES, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('list_commandes')
    else:
        form = CommandeForm(instance=commande)
    context = {'form': form}
    return render(request, 'commande/modifier_commande.html', context)


def supprimer_commande(request, pk):
    commande = get_object_or_404(Commande, id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('list_commandes')

    context = {'commande': commande}
    return render(request, 'commande/supprimer_commande.html', context)
