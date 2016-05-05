from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.template import Context
from django.views.generic import DetailView
from myhairdressings.forms import *
from .serializers import *

from rest_framework import generics
from rest_framework.reverse import reverse



def mainpage(request):
    template = get_template('index.html')
    variables = Context({
        'user': request.user,
        'titleApp': 'HairApp'
    })
    output = template.render(variables)
    return HttpResponse(output)

class HairdressingDetail(DetailView):
    model = Hairdressing
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



def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = Hairdressing(filename = request.POST['filename'],docfile = request.FILES['imgfile'])
            newimg.save(form)
            return redirect("uploads")

def register(request):
    if request.method == 'POST':

        form = RegisterUserForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username, password=password)

            user_model.email = email

            user_model.save()

            return redirect(reverse('registration.thanks', kwargs={'username': username}))
    else:

        form = RegisterUserForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def thanks_view(request, username):
    return render(request, 'registration/thanks.html', {'username': username})

#APIS

class APIHairdressingList(generics.ListAPIView):
    model = Hairdressing
    serializer_class = HairdressingSerializer

    def get_queryset(self):
        return Hairdressing.objects.all()

class APIHairdressingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Hairdressing
    serializer_class = HairdressingSerializer

    def get_queryset(self):
        return Hairdressing.objects.all()


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
