"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Doctor(models.Model):
	nom = models.CharField(max_length=150)
	specialite = models.CharField(max_length=50)
	adresse = models.TextField(null=True)
	email = models.EmailField(max_length=254)
	phone_number = models.CharField(max_length=16)
         