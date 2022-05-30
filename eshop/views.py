from django.shortcuts import render
from eshop.models import Sestava
import random
from django.views.generic import ListView, DetailView

def index(request):
    #Metoda připravuje pohled pro domovskou stránku - šablona index.html
    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    items = list(Sestava.objects.all())
    indx_sestavy = random.sample(items, 3)
    #indx_sestavy = Sestava.objects.all()[:1]

    # Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných

    context = {
        'indx_sestavy': indx_sestavy
    }
    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné
    context k zobrazení """
    return render(request, 'index.html', context=context)

class SestavaListView(ListView):
    # Nastavení požadovaného modelu
    model = Sestava
    # Pojmenování objektu, v němž budou šabloně předána data z modelu (tj. databázové tabulky)
    context_object_name = 'sestava_list'
    # Umístění a název šablony
    template_name = 'list.html'

class SestavaDetailView(DetailView):
    # Nastavení požadovaného modelu
    model = Sestava
    # Pojmenování objektu, v němž budou šabloně předána data z modelu (tj. databázové tabulky)
    context_object_name = 'sestava_detail'
    # Umístění a název šablony
    template_name = 'detail.html'
