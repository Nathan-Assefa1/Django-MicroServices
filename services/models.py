from pickle import NONE
from django.db import models
from datetime import date


class Client(models.Model):
    user_email = models.CharField(max_length=50)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

class Database(models.Model):
    user_email = models.CharField(max_length=50)
    date_of_transaction = models.CharField(max_length=50)
    amount = models.CharField(max_length=50, default=0)
