from django.contrib import admin

from .models import *


class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "category", "bid")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "bids", "user_id")


fieldsets = (
        (None, {
            'fields': ('id', 'title', 'price')
        }),
        ('Availability', {
            'fields': ('user_id', 'id', 'comment')
        }),
    )



# Register your models here.
admin.site.register(AuctionItem, AuctionItemAdmin)
admin.site.register(Comment)
admin.site.register(Bid, BidAdmin)
admin.site.register(User)
admin.site.register(WatchList)
