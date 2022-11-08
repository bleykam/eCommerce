from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from django.forms import ModelForm, forms, HiddenInput
from django.forms import MultiWidget, Textarea
from commerce import settings


class User(AbstractUser):
    pass

class WatchList(models.Model):
    choices = [(True, 'Watching'), (False, 'Watch')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_for_the_watchlist')
    item = models.ForeignKey('AuctionItem', on_delete=models.CASCADE, null=True, blank=False, related_name="item_watching")
    watched = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.item}" \
                f"{self.user}"


class AuctionItem(models.Model):
    CATEGORY_CHOICES = [
        ('', ''),
        ('1', 'Furniture'),
        ('2', 'Automobiles'),
        ('3', 'Pets'),
        ('4', 'Sporting Goods'),
        ('6', 'Electronics'),
    ]

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=False, related_name="auctions")
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=False, default=0)
    image = models.URLField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    bidcount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)



    def __str__(self):
        return f" {self.title} - " \
               f" ${self.price} "



class Bid(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=False)
    bids = models.DecimalField(max_digits=12, decimal_places=2)
    item = models.ForeignKey('AuctionItem', on_delete=models.CASCADE, null=True, blank=False, related_name="item_bidding_on")

    def __str__(self):
        return f"{self.item}"\

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_for_the_comment')
    item = models.ForeignKey('AuctionItem', on_delete=models.CASCADE, null=True, blank=False, related_name="item_commenting_on")
    comments = models.CharField(max_length=1000)


    def __str__(self):
        return f"{self.comments}   "  "\n"
        f"User: {self.user}"
