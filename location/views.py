from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Country
# Create your views here.

class GreetingView(View):
    greeting = 'good morning'

    def get(self, request):
        return HttpResponse(self.greeting)
    
