from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import AuctionItemListView, AuctionItemDetailView, AuctionItemCreateView, UserListView, \
    AuctionItemUpdateView, BookDetailView

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('<str:title>/', views.BookDetailView, name="book"),
    path("watchlist", views.WatchList, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("update_bid", views.update_bid, name="update_bid"),
    path('auctionitemslist', AuctionItemListView.as_view(), name = "auctionitemslist"),
    path('<str:pk>/auctionitems_update', AuctionItemUpdateView.as_view(), name = "auctionitems_update"),
    path('<str:title>/', AuctionItemDetailView.as_view(), name = "auctionitemdetail"),
    path('userlist', UserListView.as_view(), name = "userlist"),
    path('auctionitemform', AuctionItemCreateView.as_view(), name = "auctionitemform"),

]

