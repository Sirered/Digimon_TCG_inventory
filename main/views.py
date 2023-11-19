import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from main.forms import ItemForm
from main.models import Item
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'class' : 'PBP KKI',
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main.html', context)

def show_main_by_id(request, id):
    items = Item.objects.filter(user=request.user)
    id_item = Item.objects.filter(user=request.user).get(pk=id)
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

    context = {
        'name' : request.user.username,
        'form': form}
    return render(request, "create_item.html", context)

def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increment_amount(request, id):
    item = Item.objects.get(pk = id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_amount(request, id):
    item = Item.objects.get(pk = id)
    if item.amount>0:
        item.amount -= 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

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

def edit_item(request, id):
    product = Item.objects.get(pk = id)

    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'name' : request.user.username,
        'form': form}
    return render(request, "edit_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_item_json(request):
    item = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        category = request.POST.get("category")
        code = request.POST.get("code")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        color = request.POST.get("color")
        date_added = datetime.datetime.now()
        user = request.user

        new_item = Item(name=name, category=category, code=code, amount=amount, price=price, description=description, color = color, date_added = date_added,user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'POST':
        item = Item.objects.get(pk = id)
        item.delete()
        return HttpResponse(b"DELETED", status = 201)
    return HttpResponseNotFound()

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            category = data["category"],
            code = data["code"],
            amount = int(data["amount"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
