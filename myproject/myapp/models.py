from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Population(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return f'{self.country} - {self.year}: {self.value}'
