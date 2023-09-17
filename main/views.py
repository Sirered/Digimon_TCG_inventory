from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ItemForm
from main.models import Item

def show_main(request, id=1):
    items = Item.objects.all()
    id_item = Item.objects.get(id=id)
    context = {
        'name' : 'Galih Ibrahim Kurniawan',
        'class' : 'PBP KKI',
        'items' : items,
        'item' : id_item,
        'cardname': 'Weregarurumon',
        'category': 'Blue, Lv.7 Digimon',
        'code': 'RB-01: Resurgence Booster',
        'amount' : 0,
        'price': 4.65,
        'description' : 'a really neat card',
        'appname': 'Digimon TCG Inventory Manager'
    }

    return render(request, 'main.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
