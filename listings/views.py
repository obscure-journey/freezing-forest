from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, CreateView

from .models import *
from .forms import *

class HomeView(View):
    home_template = 'home.html'
    manage_template = 'listings/manage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            listings = Listing.objects.filter(user=request.user)
            return render_to_response(self.home_template, locals(), RequestContext(request))
        else:
            return render_to_response(self.manage_template, locals(), RequestContext(request))

class AddView(CreateView):
    model = Listing
    form_class = ListingForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(AddView, self).save(form)

    def get_success_url(self):
        return reverse('home')

class EditView(UpdateView):
    model = Listing
    form_class = ListingForm

    def get_object(self, queryset=None):
        listing = super(EditView, self).get_object(queryset)
        if listing.user != self.request.user:
            raise Http404
        return object

    def get_success_url(self):
        return reverse('home')
