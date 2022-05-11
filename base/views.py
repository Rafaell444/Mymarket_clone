from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def profilepage(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()

    count = 0

    for post in products:
        if post.host == product.host:
            count += 1

    context = {"product": product, "products": products, "length": count}
    return render(request, "profile.html", context)


def loginPage(request):
    page = "login"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password does not exist")

    context = {"page": page}
    return render(request, "login_registration.html", context)


def logoutPage(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    page = "register"
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            return redirect("home")
    context = {"form": form, "page": page}
    return render(request, "login_registration.html", context)


def home(request):
    q = request.GET.get("q") if request.GET.get('q') is not None else ""

    products = Product.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q)
    )
    category = Category.objects.all()

    for product in products:
        product.created = product.created.replace(second=0, microsecond=0)
        product.updated = product.updated.replace(second=0, microsecond=0)

    context = {"products": products, "category": category}
    return render(request, "homepage.html", context)


def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {"product": product}
    return render(request, "product.html", context)


@login_required(login_url='/login')
def createproduct(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            user = request.user
            prod = form.save(commit=False)
            prod.host = user
            prod.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "product_form.html", context)


@login_required(login_url='/login')
def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.user != product.host:
        return HttpResponse("you are not allowed here!")
    else:

        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect("home")

        context = {"form": form}

    return render(request, "product_form.html", context)


@login_required(login_url='/login')
def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.user != product.host:
        return HttpResponse("you are not allowed here !")

    if request.method == "POST":
        product.delete()
        return redirect("home")

    return render(request, "delete_product.html", context={"product": product})
