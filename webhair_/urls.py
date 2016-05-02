from django.conf.urls import include, url, patterns
from django.contrib import admin
from myhairdressings import views
from myhairdressings.views import *
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage, name='Home'),
    url(r'^login/$', 'django.contrib.auth.views.login', kwargs={'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}),
    url(r'^register/$', views.register, name='registre'),
    url(r'^citation/create/$', views.CreateCitation, name='citation_create'),
    url(r'^citation/delete/$', views.DeleteCitation, name='citation_delete'),

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

    url(
        r'thanks/(?P<username>[\w]+)/$',
        views.thanks_view,
        name='registration.thanks'
    ),
]

# API Restfull
urlpatterns += patterns('',
    url(r'^api/hairdressing/$', APIHairdressingList.as_view(), name='hairdressing_all'),
    url(r'^api/hairdressing/(?P<pk>\d+)/$', APIHairdressingDetail.as_view(), name='hairdressing_detail'),

    url(r'^api/hairdresser/$', APIHairdresserList.as_view(), name='hairdresser_all'),
    url(r'^api/hairdresser/(?P<pk>\d+)/$', APIHairdresserDetail.as_view(), name='hairdresser_detail'),

    url(r'^api/schedule/$', APIScheduleList.as_view(), name='schedule_all'),
    url(r'^api/schedule/(?P<pk>\d+)/$', APIScheduleDetail.as_view(),name='schedule_detail'),

    url(r'^api/citation/$', APICitationList.as_view(), name='citation_all'),
    url(r'^api/citation/(?P<pk>\d+)/$', APICitationDetail.as_view(), name='citation_detail'),

    url(r'^api/user/$', APIUserList.as_view(), name='user_all'),
    url(r'^api/user/(?P<pk>\d+)/$', APIUserDetail.as_view(), name='user_detail'),
)

