from rest_framework import serializers

from api.models import Auction, Bid, Comment

class AuctionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('user', 'title', 'description', 'img_url', 'base_price')

class BidModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('user', 'auction', 'amount_offered')

class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'auction', 'message')
