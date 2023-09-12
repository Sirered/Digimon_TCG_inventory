from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Galih Ibrahim Kurniawan',
        'class' : 'PBP KKI',
        'cardname': 'Weregarurumon',
        'category': 'Blue, Lv.7 Digimon',
        'set_release': 'RB-01: Resurgence Booster',
        'amount' : 0,
        'price': 4.65,
        'description' : 'a really neat card'
    }

    return render(request, 'main.html', context)
