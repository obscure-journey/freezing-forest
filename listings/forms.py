from django.forms import ModelForm

from .models import *

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        exclude = ('user',)
