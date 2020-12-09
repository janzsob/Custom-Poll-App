from django.db import models
from django.utils.timezone import now
from datetime import datetime


class Students(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    major = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    subject = models.CharField(max_length=100)
    post_text = models.TextField("Text")
    post_date = models.DateTimeField("Posted Date", auto_now_add=True)
    update_date = models.DateTimeField("Updated Date", auto_now=True)

    def __str__(self):
        return self.subject


class Listings (models.Model):
    condition_types = [
        ("USED", "Used"),
        ("NEW", "New")
    ]

    delivery_types = [
        ("SHIPMENT", "Shipment"),
        ("PICK UP", "Pick up")
    ]

    title = models.CharField(max_length=100)
    condition = models.CharField(
        max_length=50, choices=condition_types, default="NEW")
    delivery = models.CharField(
        max_length=50, choices=delivery_types)
    price = models.FloatField()
    list_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
