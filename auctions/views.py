from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, View
from django.views import generic
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ProcessFormView
from django.shortcuts import get_object_or_404

from .models import User, AuctionItem, Bid, BidForm, WatchList

User = get_user_model()
def index(request):
    active_listings = AuctionItem.objects.all()
    context = {'active_listings': active_listings}
    print(("I \u2764 Django") )

    return render(request, "auctions/index.html", context)

class UserListView(ListView):
    model = User
    fields = '__all__'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['bid'] = str(User.bid_set)
        return context


@login_required()
def UserDetailView(request):
    template_name = 'auctions/user_detail.html'
    user = request.user
    person = User.objects.all()
    print(user)
    if user.id is None:
        return HttpResponseRedirect(reverse('login'))
    context = {"user":user, "person":person}
    return render(request, "auctions/user_detail.html", context)




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
        stuff=list(AuctionItem.objects.all())
        items = AuctionItem.objects.all().order_by('category')
        context = {'items': items, "stuff":stuff}

        return render(request, "auctions/categories.html", context)

def watchlist(request, *args, **kwargs):
    item= get_object_or_404(AuctionItem, pk=kwargs['title'])
    context = {'item': item}

    if request.method=="POST":

        print(item, "item")
        print(request.META.get('HTTP_REFERER'))


        return HttpResponse('success')


class AuctionItemListView(ListView):
    model = AuctionItem
    pk_url_kwarg = 'title'

class WatchListView(ListView):
    model = WatchList
    fields = '__all__'


class AuctionItemCreateView(CreateView):
    model = AuctionItem
    fields = '__all__'

    def get_success_url(self):
        return reverse('auctionitemslist')


class AuctionItemUpdateView(UpdateView):
    model = AuctionItem
    fields = '__all__'

    def get_success_url(self):
        return reverse('auctionitemslist')



def BookDetailView(request, *args, **kwargs):
    item= get_object_or_404(AuctionItem, pk=kwargs['title'])
    item.bid = BidForm(initial={'user': request.user})
    context = {'item': item}
    if 'placebid' in request.POST:
        form = BidForm(request.POST)
        print(form)
        if float(request.POST.get('bids')) > int(item.price):
            if form.is_valid():
                form.user = request.user
                print("USER =:", form.user)
                bids = form.cleaned_data['bids']
                form.save()
                print("SAVED", form.user)
            item.price = request.POST.get('bids')
            item.bidcount +=1
            item.save()


    return render(request, "auctions/book.html", context)



class AuctionItemDetailView(DetailView):
    model = AuctionItem
    pk_url_kwarg = 'title'
    form = BidForm()