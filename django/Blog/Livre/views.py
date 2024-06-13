from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre
from .forms import LivreForm
from .filters import LivreFilter


# Create your views here.
def liste_livre(request):
    livres = Livre.objects.all()
    livrefilter=LivreFilter(request.GET,queryset=livres)
    context = {'livrefilter': livrefilter}
    return render(request, 'livre/liste_livre.html', context)


def detail_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    context = {'livre': livre}
    return render(request, 'livre/detail_livre.html', context)


# def ajouter_livre(request):
#     print("1")
#     if request.method=='POST':
#         print("2")
#         form=LivreForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             print("3")
#             return redirect('index')
#     else:
#         form=LivreForm()
#         context={'form':form}
#         print("4")
#     return render(request,'livre/ajouter_livre.html',context)
#

def ajouter_livre(request):
    print("apel au ajouter")
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('livre')
    else:
        form = LivreForm()
        context = {'form': form}
    return render(request, 'livre/ajouter_livre.html', context)


def modifier_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('livre')
    else:
        form = LivreForm(instance=livre)
    context = {'form': form}
    return render(request, 'livre/modifier_livre.html', context)


def supprimer_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == "POST":
        livre.delete()
        redirect('livre')
    context = {'livre': livre}
    return render(request, 'livre/supprimer_livre.html', context)
