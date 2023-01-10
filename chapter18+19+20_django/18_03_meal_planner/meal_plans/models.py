from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name