from django import forms
from django.forms.models import ModelForm

from auctions import models

class WatchListForm(forms.Form):
    watchitem = forms.CharField(label="New Item")

