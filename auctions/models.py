from django.contrib.auth.models import User, AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from django.forms import ModelForm, forms, HiddenInput
from django.forms import MultiWidget, Textarea
from commerce import settings


class User(AbstractUser):
    pass

class Comment(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_for_the_comment')
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.comments

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']


class WatchList(models.Model):
    choices = [(True, 'Watching'), (False, 'Watch')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_for_the_watchlist')
    auctions = models.ManyToManyField('AuctionItem', related_name='auctions_in_the_watchlist', blank=True)
    watched = models.BooleanField(default=False)
    def __str__(self):
        return f": ${self.auctions.name}"


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
    bidcount = models.IntegerField(default=0)

    def __str__(self):
        return f" Title: {self.title} " \
               f" price: {self.price} "



class Bid(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=False)
    bids = models.DecimalField(max_digits=12, decimal_places=2)
    item = models.ForeignKey('AuctionItem', on_delete=models.CASCADE, null=True, blank=False, related_name="item_bidding_on")

    def __str__(self):
        return f" Current Bid: ${self.bids}"\
                f" user: {self.user}"\
                f" item: {self.item}"

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bids', 'user', 'item']

        widgets = {
            'bids': Textarea(attrs={'cols': 20, 'rows': 1}),
            'user': HiddenInput(),


         }