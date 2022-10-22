from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import MultiWidget, Textarea

from commerce import settings

CATEGORY_CHOICES = [
        ('', ''),
        ('1', 'Furniture'),
        ('2', 'Automobiles'),
        ('3', 'Pets'),
        ('4', 'Sporting Goods'),
        ('6', 'Electronics'),
    ]

class User(AbstractUser):
    watchlist_counter = models.IntegerField(blank=True)

    pass


class Comment(models.Model):
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.comments

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']


class Bid(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
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





class AuctionItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=False)
    image = models.URLField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    form = CommentForm()
    bid = BidForm()



    def __str__(self):
        return f" Title: {self.title}" \
               f" Description: {self.description}  " \
               f" {self.image}" \
               f"Starting Price: ${self.price} "



