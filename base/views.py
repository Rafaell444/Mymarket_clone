from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.

# products = [
#     {"id": 1, "name": "piano"},
#     {"id": 2, "name": "guitar"},
#     {"id": 3, "name": "puppy"},
#
# ]


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "homepage.html", context)


def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {"product": product}
    return render(request, "product.html",context)
