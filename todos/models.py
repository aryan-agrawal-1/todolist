from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todos(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 500)
    priority = models.IntegerField()
    date = models.DateField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    isDone = models.BooleanField(default = False)