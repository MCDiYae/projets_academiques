from django.shortcuts import render, get_object_or_404, redirect


from .forms import LivreForm
from .models import Livre
from .filters import LivreFilter
# Create your views here.


def home(request):
    livres = Livre.objects.all()
    livrefilter = LivreFilter(request.GET, queryset=livres)
    context = {'livrefilter': livrefilter}
    return render(request, 'livre/home.html', context)


def detail_livre(request, pk):
    livre = get_object_or_404(Livre, id=pk)
    context = {'livre': livre}
    return render(request, 'livre/detail_livre.html', context)


def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivreForm()
        context = {'form': form}
        return render(request, 'livre/ajouter_livre.html', context)


def modifier_livre(request, pk):
    livre = get_object_or_404(Livre, id=pk)
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivreForm(instance=livre)
    context = {'form': form}
    return render(request, 'livre/modifier_livre.html', context)


def supprimer_livre(request, pk):
    livre = get_object_or_404(Livre, id=pk)
    if request.method == 'POST':
        livre.delete()
        return redirect('home')

    context = {'livre': livre}
    return render(request, 'livre/supprimer_livre.html', context)
