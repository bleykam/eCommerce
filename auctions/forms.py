from django import forms
from django.forms.models import ModelForm
from .models import User, AuctionItem, Bid, WatchList, Comment

from django.forms import MultiWidget, Textarea

class AuctionItemCreateForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        exclude = ('user',)