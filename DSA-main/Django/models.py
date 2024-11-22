from django.db import models

class Aerodrome(models.Model):
    name = models.CharField(max_length = 100)
    Latitude = models.DecimalField(decimal_places=4)
    Longitude = models.DecimalField(decimal_places=4)

    class Meta:
        db_table = "aerodrome"
        managed = False
