from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, RedirectView
from django.contrib.auth.decorators import login_required, user_passes_test


class HomeView(TemplateView):
    template_name = 'home.html'
