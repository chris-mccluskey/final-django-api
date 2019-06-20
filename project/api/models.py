from django.db import models
from django.conf import settings


class Auction(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img_url = models.URLField(max_length=200)
    base_price = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.title

class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount_offered = models.IntegerField(null=True, blank=True)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    create = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title 
