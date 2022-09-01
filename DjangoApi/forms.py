
from django import forms
from .models import Language
from django.core.validators import RegexValidator
import re
class LangaugeForm(forms.ModelForm):
    class Meta:
              model = Language
              fields = "__all__"

    language = forms.CharField(label='Enter Language syntax',validators=[RegexValidator('^([^0-9]*)$')])
