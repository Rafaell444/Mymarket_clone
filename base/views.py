from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category
from .forms import ProductForm


# Create your views here.

# products = [
#     {"id": 1, "name": "piano"},
#     {"id": 2, "name": "guitar"},
#     {"id": 3, "name": "puppy"},
#
# ]


def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {"products": products, "category": category}
    return render(request, "homepage.html", context)


def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {"product": product}
    return render(request, "product.html", context)


def createproduct(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "product_form.html", context)


def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}

    return render(request, "product_form.html",context)
