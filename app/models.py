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
	phone_number1 = models.CharField(max_length=16)
	anecdote = models.TextField(null=True)    
	
class Hospital(models.Model):
	nom = models.CharField(max_length=200)
	quartier = models.CharField(max_length=75)
	adresse = models.TextField(null=True)
	email = models.EmailField(max_length=254)
	phone_number1 = models.CharField(max_length=16)
	phone_number2 = models.CharField(max_length=16)
	specialite = models.CharField(max_length=50)