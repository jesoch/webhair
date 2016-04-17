from django.conf.urls import include, url
from django.contrib import admin
from myhairdressings.views import *
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, UpdateView
from django.shortcuts import get_object_or_404


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage, name='Home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),

    # Hairdressings
    url(r'^hairdressing/$',
        ListView.as_view(
            queryset=AdminHairDressing.objects.all(),
            context_object_name='HairdressingList',
            template_name='hairdressingslist.html'),
        name='hairdressingslist'),

    # Hairdressing Details
    url(r'^hairdressing/(?P<pk>\d+)/$',
        HairdressingDetail.as_view(),
        name='hairdressing_detail'),

    #Hairdresser Details
    url(r'^hairdressing/(?P<pkr>\d+)/hairdresser/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Hairdresser,
            template_name='hairdresser_detail.html'),
        name='hairdresser_detail'),

    # User Citations
    url(r'^citations/$',
        ListView.as_view(
            queryset=Citation.objects.all(),
            context_object_name='CitationsList',
            template_name='citations.html'),
        name='citations'),

    # Create citation
    url(r'^citation/create/$',
        CitationCreate.as_view(),
        name='citation_create'),
]
