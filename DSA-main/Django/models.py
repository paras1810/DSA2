'''
Django ORM(Object-Relational Mapper) powerful feature of Django web framework allow developer to interact 
with relational DBs using Python objects, rather writing SQL query.

It maps models to DB tables, so you create, retrieve, update or delete records using Python code.
'''
from django.db import models

class Aerodrome(models.Model):
    name = models.CharField(max_length = 100)
    Latitude = models.DecimalField(decimal_places=4)
    Longitude = models.DecimalField(decimal_places=4)

    class Meta:
        db_table = "aerodrome"
        managed = False
