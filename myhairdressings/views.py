from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import AdminHairDressing, Hairdresser, Citation
from django.contrib.auth.models import User
from .forms import CitationForm
from django.template.loader import get_template
from django.template import Context
from django.views.generic import DetailView, ListView, UpdateView


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

class CitationCreate(CreateView):
    model = Citation
    template_name = 'hairdresser_detail.html'
    form_class = CitationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.id_schedule = Citation.objects.get(id=self.kwargs['pk'])
        print (form.instance.id_schedule)
        return super(CitationCreate, self).form_valid(form)