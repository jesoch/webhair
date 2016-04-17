from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, request
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import AdminHairDressing, Hairdresser, Citation, Schedule
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from django.views.generic import DetailView, ListView, UpdateView
from .serializers import HairdressingSerializer, HairdresserSerializer, ScheduleSerializer, CitationSerializer, UserSerializer

from django.views.generic.base import TemplateResponseMixin

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.

def mainpage(request):
    template = get_template('index.html')
    variables = Context({
        'user': request.user
    })
    output = template.render(variables)
    return HttpResponse(output)

class HairdressingDetail(DetailView):
    model = AdminHairDressing
    template_name = 'hairdressing_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HairdressingDetail,self).get_context_data(**kwargs)
        return context

class HairdresserDetail(DetailView):
    model = Hairdresser
    template_name = 'hairdresser_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HairdresserDetail,self).get_context_data(**kwargs)
        return context

class Citations(DetailView):
    model = Citation
    template_name = 'citations.html'

    def get_context_data(self, **kwargs):
        context = super(Citations,self).get_context_data(**kwargs)
        return context

def CreateCitation(request):
    u = request.POST.get('user')
    us = User.objects.get(username=u)
    s = request.POST.get('schedule')
    sc = Schedule.objects.get(pk=s)

    c = Citation(id_user=us, id_schedule=sc)
    c.save()
    return redirect('/citations?a=1')

def DeleteCitation(request):
    id_citation = request.POST.get('id_citation')
    citation = Citation.objects.get(id=id_citation)
    citation.delete()
    return redirect('/citations')


#APIS

class APIHairdressingList(generics.ListAPIView):
    model = AdminHairDressing
    serializer_class = HairdressingSerializer

    def get_queryset(self):
        return AdminHairDressing.objects.all()

class APIHairdressingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = AdminHairDressing
    serializer_class = HairdressingSerializer

    def get_queryset(self):
        return AdminHairDressing.objects.all()


class APIHairdresserList(generics.ListAPIView):
    model = Hairdresser
    serializer_class = HairdresserSerializer

    def get_queryset(self):
        return Hairdresser.objects.all()

class APIHairdresserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Hairdresser
    serializer_class = HairdresserSerializer

    def get_queryset(self):
        return Hairdresser.objects.all()

class APIScheduleList(generics.ListAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()

class APIScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.all()

class APICitationList(generics.ListAPIView):
    model = Citation
    serializer_class = CitationSerializer

    def get_queryset(self):
        return Citation.objects.all()

class APICitationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Citation
    serializer_class = CitationSerializer

    def get_queryset(self):
        return Citation.objects.all()


class APIUserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class APIUserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()