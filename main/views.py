from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ItemFormForm
from main.models import Item

def show_main(request):
    context = {
        'name' : 'Galih Ibrahim Kurniawan',
        'class' : 'PBP KKI',
        'cardname': 'Weregarurumon',
        'category': 'Blue, Lv.7 Digimon',
        'set_release': 'RB-01: Resurgence Booster',
        'amount' : 0,
        'price': 4.65,
        'description' : 'a really neat card',
        'appname': 'Digimon TCG Inventory Manager'
    }

    return render(request, 'main.html', context)
