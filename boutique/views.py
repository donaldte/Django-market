from django.shortcuts import render

# Create your views here.


def store(request):
    return render(request, 'boutique/store.html')


def cart(request):
    return render(request, 'boutique/cart.html')

def checkout(request):
    return render(request, 'boutique/checkout.html')        