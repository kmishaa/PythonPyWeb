from django.db import models
from datetime import date, datetime
from django.core.validators import RegexValidator

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()