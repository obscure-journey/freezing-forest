from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('listings.views',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^add/$', login_required(AddView.as_view()), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(EditView.as_view()), name='edit'),
)
