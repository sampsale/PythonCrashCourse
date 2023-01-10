from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    # Home page for Pizzas
    return render(request, 'pizzas/index.html')

def pizzas(request):
    # Show all pizzas
    pizzas = Pizza.objects.all()
    print(f"\n\t{pizzas}")
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    # Show a single pizza and all its toppings
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings.all()
    context = {'topic': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)