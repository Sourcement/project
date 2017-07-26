from django.db import models
from datetime import datetime

# Create your models here.

class Person(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.email

