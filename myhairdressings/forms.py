from django.forms import forms
from myhairdressings.models import Citation

class CitationForm(forms.Form):
    class Meta:
        model = Citation
        fields = ('id_schedule', 'id_user',)