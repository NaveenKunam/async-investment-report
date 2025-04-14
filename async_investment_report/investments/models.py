from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Property(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Investment(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateField()
