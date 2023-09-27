import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ItemForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'class' : 'PBP KKI',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }

    if request.method == "POST":
        print(request.POST)
        if 'increment' in request.POST:
            item = items.get(id = request.POST.get('increment'))
            increment_amount(item)
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'decrement' in request.POST:
            item = items.get(id = request.POST.get('decrement'))
            decrement_amount(item)
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'delete' in request.POST:
            item = items.get(id = request.POST.get('delete'))
            item.delete()
            return HttpResponseRedirect(reverse('main:show_main'))

    return render(request, 'main.html', context)

def show_main_by_id(request, id):
    items = Item.objects.filter(user=request.user)
    id_item = Item.objects.filter(user=request.user).get(id=id)
    context = {
        'name' : request.user.username,
        'class' : 'PBP KKI',
        'items' : items,
        'item': id_item,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main_id.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increment_amount(item):
    item.amount += 1
    item.save()

def decrement_amount(item):
    if item.amount>0:
        item.amount -= 1
    item.save()


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
