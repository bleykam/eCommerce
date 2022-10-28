from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import MultiWidget, Textarea

from commerce import settings


class User(AbstractUser):
    pass
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watchlist = models.TextField(max_length=500, blank=True)
    bids = models.CharField(max_length=30, blank=True)


class Comment(models.Model):
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.comments

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']



class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bids = models.DecimalField(max_digits=12, decimal_places=2)


    def __str__(self):
        return f" Current Bid: ${self.bids}"

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bids']
        widgets = {
            'bids': Textarea(attrs={'cols': 20, 'rows': 1}),
        }

class Watch(models.Model):
    watched =  models.BooleanField(default=False)


    def __str__(self):
        return f" Current Bid: ${self.bids}"

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bids']
        widgets = {
            'bids': Textarea(attrs={'cols': 20, 'rows': 1}),
        }




class AuctionItem(models.Model):
    CATEGORY_CHOICES = [
        ('', ''),
        ('1', 'Furniture'),
        ('2', 'Automobiles'),
        ('3', 'Pets'),
        ('4', 'Sporting Goods'),
        ('6', 'Electronics'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=False, default=0)
    image = models.URLField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    form = CommentForm()
    bid = BidForm()


    def categories_verbose(self):
        return f" verbose: {self.get_category_display}"
    def __str__(self):
        return f" Title: {self.title} " \




