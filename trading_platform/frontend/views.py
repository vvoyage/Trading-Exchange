from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def orders(request):
    return render(request, 'orders.html')

def balances(request):
    return render(request, 'balances.html')
