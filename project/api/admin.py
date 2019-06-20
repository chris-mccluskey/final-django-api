from django.contrib import admin
from .models import Auction, Bid, Comment
# Register your models here.
@admin.register(Auction)
class AuctionrAdmin(admin.ModelAdmin):
    pass

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
