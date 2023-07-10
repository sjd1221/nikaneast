from django.db import models

class Contact(models.Model):
    Name = models.CharField(max_length=300)
    Name2 = models.CharField(max_length=300)
    Number = models.CharField(max_length=300)
    Floor = models.CharField(max_length=300)