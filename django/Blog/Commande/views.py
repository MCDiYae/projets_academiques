from django.shortcuts import render, HttpResponse, redirect

from Commande.models import Commande


# Create your views here.
def list_commande(request):
    return render(request, 'commande/liste_commande.html')


def supprimer_commande(request, id):
    commande = Commande.objects.get(id=id)
    if request.method == "POST":
        commande.delete()
        redirect('/')
    context = {'commande': commande}
    return render(request, 'commande/supprimer_commande.html', context)
