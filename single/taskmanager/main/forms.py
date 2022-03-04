from .models import Sample
from django.forms import ModelForm


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = ["__all__"]
