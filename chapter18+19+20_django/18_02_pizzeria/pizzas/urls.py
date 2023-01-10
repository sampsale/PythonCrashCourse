# Defines URL patterns for pizzas

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
    # Toppings page for a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]