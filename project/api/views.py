
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Auction, Bid, Comment
from api.serializers import AuctionModelSerializer, BidModelSerializer, CommentModelSerializer

class AuctionModelViewSet(viewsets.ModelViewSet):

    serializer_class = AuctionModelSerializer
    queryset = Auction.objects.all()

class BidModelViewSet(viewsets.ModelViewSet):

    serializer_class = BidModelSerializer
    queryset = Bid.objects.all()

class CommentModelViewSet(viewsets.ModelViewSet):

    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
