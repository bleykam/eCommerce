from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.list import ListView, View
from django.views import generic
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ProcessFormView
from django.shortcuts import get_object_or_404
from .forms import WatchListForm
from .models import User, AuctionItem, Bid

def index(request):
    active_listings = AuctionItem.objects.all()
    context = {'active_listings': active_listings}

    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def update_bid(request):
    if request.method =="POST":

        Bid = BidForm(request.POST)
        if BidForm.is_valid():
            Bid.save()

        obj = AuctionItem.objects.get()
        obj.save()
        return render(request, "auctions/auctionitem_details.html", {"Bid": Bid})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def categories(request):
    active_listings = AuctionItem.objects.all()
    context = {'active_listings': active_listings}

    return render(request, "auctions/categories.html")

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'



class AuctionItemForm(ModelForm):
    class Meta:
        model = AuctionItem
        fields = ['price']


class AuctionItemDetailView(DetailView):
    model = AuctionItem
    pk_url_kwarg = 'title'
    form = BidForm()


    def get_success_url(self):
        return reverse('auctionitemslist')



class AuctionItemListView(ListView):
    model = AuctionItem
    pk_url_kwarg = 'title'

class UserListView(ListView):
    model = User


class AuctionItemCreateView(CreateView):
    model = AuctionItem
    fields = '__all__'

    def get_success_url(self):
        return reverse('auctionitemslist')


class AuctionItemUpdateView(UpdateView):
    model = AuctionItem
    form = BidForm
    fields = '__all__'

    def get_success_url(self):
        return reverse('auctionitemslist')



def BookDetailView(request, *args, **kwargs):
    item= get_object_or_404(AuctionItem, pk=kwargs['title'])
    context = {'item': item}

    if request.method == 'POST':
        form = BidForm(request.POST)
        if float(request.POST.get('bids')) > int(item.price):
            if form.is_valid():
                form.save()

            item.price = request.POST.get('bids')
            item.save()
            return render(request, "auctions/book.html", context)






def WatchList(request):
    return render(request, 'auctions/watchlist.html', {})

    def get_success_url(self):
        return reverse('book')