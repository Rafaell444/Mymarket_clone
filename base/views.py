from django.db.models import Q
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
    q = request.GET.get("q") if request.GET.get('q') is not None else ""

    products = Product.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
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
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}

    return render(request, "product_form.html", context)


def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        product.delete()
        return redirect("home")

    return render(request, "delete_product.html", context={"product": product})
