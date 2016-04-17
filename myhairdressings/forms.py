from django.forms import ModelForm
from .models import Citation

class CitationForm(ModelForm):
    class Meta:
        model = Citation
        exclude = ('date',)