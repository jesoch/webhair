from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import AdminHairDressing, client


# Create your views here.
def post_list(request):
        return reverse(request, 'hairdressing/post_list.html', {})