from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class GreetingView(View):
    greeting = 'good morning'

    def get(self, request):
        return HttpResponse(self.greeting)
    
