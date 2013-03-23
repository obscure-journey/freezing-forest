from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^plan/$', 'plan', name='plan'),
    url(r'^billing/$', 'billing', name='billing'),
    url(r'^brokers/$', 'brokers', name='brokers'),
    url(r'^password/$', 'change_password', name='change_password'),
)
