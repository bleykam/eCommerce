from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import UserDetailView, AuctionItemListView,  AuctionItemCreateView, \
    AuctionItemUpdateView,  WatchListView, ClosedAuctionItemListView

urlpatterns = [

    path("", views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('closedauctionitemlist', ClosedAuctionItemListView.as_view(),  name = "closedauctionitemlist"),
    path('user_detail', views.UserDetailView, name = "user_detail"),
    path('path', WatchListView.as_view(), name = "watchlist_list"),
    path("categories", views.categories, name="categories"),
    path('auctionitemslist', AuctionItemListView.as_view(), name = "auctionitemslist"),
    path('<str:title>/', views.AuctionItemDetailView, {"active": True}, name="auctionitemdetail"),
    path('<str:pk>/auctionitem_update', AuctionItemUpdateView.as_view(), name = "auctionitems_update"),
    path('auctionitemform', AuctionItemCreateView.as_view(), name = "auctionitemform"),
    path("comment/<int:item_id>", views.comment, name="comment"),

]

