# Generated by Django 4.1.5 on 2023-01-03 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]