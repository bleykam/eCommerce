from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import UserListView, AuctionItemListView, AuctionItemDetailView, AuctionItemCreateView, UserDetailView, \
    AuctionItemUpdateView, BookDetailView, WatchListView

urlpatterns = [
    path("", views.index, name='index'),
    path('<str:title>/', views.BookDetailView, name="book"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('path', WatchListView.as_view(), name = "watchlist_list"),
    path('<str:title>/', views.watchlist, name="watchlist"),
    path('user_list', UserListView.as_view(), name = "user_list"),
    path('<str:title>/', views.BookDetailView, name="book"),
    path("categories", views.categories, name="categories"),
    path('auctionitemslist', AuctionItemListView.as_view(), name = "auctionitemslist"),
    path('<str:pk>/auctionitems_update', AuctionItemUpdateView.as_view(), name = "auctionitems_update"),
    path('<str:title>/', AuctionItemDetailView.as_view(), name = "auctionitemdetail"),
    path('path', UserDetailView, name = "user"),
    path('auctionitemform', AuctionItemCreateView.as_view(), name = "auctionitemform"),

]

