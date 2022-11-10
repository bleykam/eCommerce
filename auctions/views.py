from django.contrib import messages
import django.contrib.messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ProcessFormView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from np.magic import np

from .forms import AuctionItemCreateForm
from .models import User, AuctionItem, Bid, WatchList, Comment


User = get_user_model()
def index(request):
    # get QuerySet of all items on auction
    active_listings = AuctionItem.objects.filter(active =True)
    #add queryset to context available to template
    listing = list(AuctionItem.objects.filter(active=True).values())
    feature =np.random.choice(listing)
    context = {'active_listings': active_listings, "feature":feature}
    return render(request, "auctions/index.html", context)

class UserDeatilView(DetailView):
    model = User
    fields = '__all__'
class ClosedAuctionItemListView(ListView):
    model = AuctionItem
    template = 'closedauctionitem_list.html'
    #only show closed listings
    queryset = AuctionItem.objects.filter(active=False)

@login_required(login_url='login')
def UserDetailView(request):
    # get current user object
    user= request.user
    #get QuerySet of bids for current user from bid model using foreign key
    bid = user.bid_set.all().order_by('item')
    #get Queryset, using related name,of all comments posted by current user
    comment = user.user_for_the_comment.all()
    watching = user.user_for_the_watchlist.all()
    # get Queryset of lisitngs the current user created
    listings =  AuctionItem.objects.filter(user=request.user)
    #set context available to template
    context = {"user": user, "bid":bid, "comment":comment, "watching":watching, "listings":listings }

    #Render the HTML template with data in the context variable
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
    #get QuerySet of all auction items ordered by category
        items = AuctionItem.objects.all().order_by('category')
        context = {'items': items}
        return render(request, "auctions/categories.html", context)

def comment(request, *args, **kwargs):
    #get QuerySet of auction listings
    listing = AuctionItem.objects.get(pk=kwargs['item_id'])
    #creates new comment object
    if request.method=="POST":
        remark = Comment.objects.create(user=request.user)
        remark.item=listing
        remark.comments =request.POST.get('comment')
        remark.save()
        messages.success(request, 'Comment successfully added.')
        # Reloads page
        return HttpResponseRedirect(reverse("auctionitemdetail", kwargs={'title':listing.id}))

class AuctionItemListView(ListView):
    model = AuctionItem
    #only show active listings
    queryset = AuctionItem.objects.filter(active=True)

class WatchListView(ListView):
    model = WatchList
    fields = '__all__'

class AuctionItemCreateView(LoginRequiredMixin, CreateView):
    model = AuctionItem
    form_class = AuctionItemCreateForm
    login_url = 'login'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('auctionitemslist')

class AuctionItemUpdateView(LoginRequiredMixin, UpdateView):
    model = AuctionItem
    form_class = AuctionItemCreateForm
    login_url = 'login'

    #populates form with current user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #require user to be owner of post to edit it.
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(AuctionItemUpdateView, self).dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('auctionitemslist')

def AuctionItemDetailView(request, *args, **kwargs):
    template = 'auctionitemdetail.html'
    #gets AuctionItem object for auction with "title"
    item= get_object_or_404(AuctionItem, pk=kwargs['title'])
    #gets all coments for current auction
    bid = Bid.objects.filter(item=kwargs['title'])
    comment = Comment.objects.filter(item=kwargs['title'])
    list = WatchList.objects.filter(user=request.user)
    context = {'item': item, "comment":comment, "list":list}
    if item.active == False:
        highestBid = Bid.objects.filter(item=kwargs['title']).order_by('-bids')[0]
        context = {'item': item, "comment": comment, "list": list, "highestBid": highestBid}
        return render(request, "auctions/auctionitemdetail.html", context)

    elif request.user.is_authenticated:
        if 'placebid' in request.POST:
            if float(request.POST.get('placebid')) > int(item.price):
                bid = Bid.objects.create(bids=request.POST.get('placebid'))
                bid.user=request.user
                bid.item=item
                bid.save()
                item.price = request.POST.get('placebid')
                item.bidcount +=1
                item.save()
            elif float(request.POST.get('placebid')) < int(item.price):
                messages.error(request, f"Enter Bid Higher than ${item.price}.")
                return redirect(request.path_info)

        elif "watch" in request.POST:
            if list.filter(item=item.id).exists():
                WatchList.objects.filter(item=item.id).delete()
                messages.success(request, "Auction successfully removed from Watchlist")
                return redirect(request.path_info)
            else:
                watching = WatchList.objects.create(user=request.user)
                watching.item=item
                watching.watched=True
                watching.save()
                messages.success(request, "Auction successfully added to Watchlist")
    else:
            return render(request, "auctions/login.html", {
                "message": "Must be logged in."
            })
    return render(request, "auctions/auctionitemdetail.html", context)

