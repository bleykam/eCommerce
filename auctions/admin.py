from django.contrib import admin

from .models import *

class BidInline(admin.TabularInline):
    model = Bid
class AuctionItemAdmin(admin.ModelAdmin):
    inlines = [BidInline]
    list_display = ("id", "title", "description", "price", "category", "user")

class BidAdmin(admin.ModelAdmin):

    list_display = ("id", "bids", "user", "item")


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
