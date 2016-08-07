from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import View
from django.template import loader
from django.shortcuts import get_object_or_404, render
import datetime

def index(request):
    product_list = Product.objects.all()[:3]
    template = loader.get_template('products/index.html')
    context = {
            'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))

def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

def detail(request, product_id):
        product = get_object_or_404(Product, pk = product_id)
        return  render(request,'products/product_detail.html', {'product': product}) 
