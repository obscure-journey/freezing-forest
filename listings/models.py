from django.contrib.auth.models import User
from django.db import models

from .choices import *

def listing_picture_upload_to(instance, filename):
    return '/'.join(['images', instance.id, filename])

class Listing(models.Model):
    # user
    user = models.ForeignKey(User)
    # flags
    is_sold = models.BooleanField(default=False)
    push_nyt = models.BooleanField(default=False)
    # real fields
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=39)
    apt_number = models.CharField('apartment/unit number', max_length=50, blank=True)
    headline = models.CharField(max_length=99, blank=True)
    cross_street = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150)
    state = models.CharField('state/province', max_length=2, choices=STATE_CHOICES)
    zip_code = models.CharField('zip/postal code', max_length=6)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES, default='USA')
    price = models.DecimalField(decimal_places=2, max_digits=15, blank=True)
    maintenance = models.DecimalField('monthly maintenance', decimal_places=2, max_digits=15, blank=True, null=True)
    bedrooms = models.IntegerField('number of bedrooms', blank=True, null=True)
    lat = models.FloatField('latitude')
    lon = models.FloatField('longitude')
    image = models.FileField(upload_to=listing_picture_upload_to, blank=True, null=True)

    def complete(self):
        if self.monthly_maintenance and self.bedrooms and self.price:
            return True
        return False

    def __unicode__(self):
        return self.user.username + "'s listing at " + self.street_number + " " + self.street_name 
