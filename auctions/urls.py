from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import UserListView, AuctionItemListView, AuctionItemDetailView, AuctionItemCreateView, UserDetailView, \
    AuctionItemUpdateView, BookDetailView

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('user_list', UserListView.as_view(), name = "user_list"),
    path('<str:title>/', views.BookDetailView, name="book"),
    path("watchlist", views.Watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path('auctionitemslist', AuctionItemListView.as_view(), name = "auctionitemslist"),
    path('<str:pk>/auctionitems_update', AuctionItemUpdateView.as_view(), name = "auctionitems_update"),
    path('<str:title>/', AuctionItemDetailView.as_view(), name = "auctionitemdetail"),
    path('ser/', UserDetailView.as_view(), name = "user"),
    path('auctionitemform', AuctionItemCreateView.as_view(), name = "auctionitemform"),

]

