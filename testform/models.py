from django.db import models

class Property (models.Model):
    property_types = [
        ("HOUSE", "House"),
        ("FLAT", "Flat")
    ]

    types = models.CharField("Type", max_length=100, choices=property_types, default="HOUSE")
    price = models.FloatField()
    size = models.FloatField("Size(m2)")
    city = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.owner
