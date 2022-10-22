from django.contrib import admin

from .models import *


class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "category", "image")



# Register your models here.
admin.site.register(AuctionItem, AuctionItemAdmin)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(User)
