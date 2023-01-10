from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='toppings')
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name