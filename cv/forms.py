# forms.py
from django import forms
# from .models import *
  
class BrainScansForm(forms.Form):
    brain_scan_img = forms.ImageField(label='MRI Scan')
