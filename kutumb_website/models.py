# familytreeapp/models.py

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='family_photos/')