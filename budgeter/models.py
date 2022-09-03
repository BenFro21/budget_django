from django.db import models
from datetime import datetime

# Create your models here.

class Budget(models.Model):
    title = models.CharField(max_length=100, default='no title')
    # date_created = models.DateField(("Date"), default=datetime.date)
    budget_for = models.CharField(max_length=100, default='Misc.')
    income = models.IntegerField(default=0, blank=True, editable=True)
    total = models.IntegerField(blank=True, editable=True)
    
    def __str__(self):
        return self.title
    
    
class Expenses(models.Model):
    type_choices = (
       ('Misc', 'Miscellaneous'),
       ('Car', 'Car'),
       ('Elec', 'Electric'),
       ('Util', 'Utilites'),
       ('Food','Grocery'),
       ('Fun', 'Entertainment'),
       ('Kids', 'Kids'),
       ('Pets', 'Pets') 
    )
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    # date_created = models.DateField(("Date"), default=datetime.date)
    biller = models.CharField(max_length=100)
    amount_planned = models.IntegerField(default=0, blank=True, editable=True)
    amount_actual = models.IntegerField(default=0, blank=True, editable=True)
    type_bill = models.CharField(max_length=4, choices=type_choices)
    
    def __str__(self):
       return f"{self.title} part of {self.budget} budget" 
       