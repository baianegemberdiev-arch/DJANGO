from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model}"


class Bicycle(models.Model):
    brand = models.CharField(max_length=55)
    type = models.CharField(max_length=55)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} ({self.type})"


