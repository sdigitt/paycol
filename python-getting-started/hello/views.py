from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Bid

# Create your views here.

class DashView(ListView):
	template_name = "dash.html"
	model = Bid

