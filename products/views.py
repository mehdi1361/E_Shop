from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from django.views.generic import View
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
import datetime


@cache_page(60 * 15)
def index(request):
    product_list = Product.objects.all()[:3]
    template = loader.get_template('products/index.html')
    context = {
            'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))

@cache_page(60 * 15)
def category_list(request):
    category_list = Category.objects.all()
    template = loader.get_template('products/category.html')
    context = {
            'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))

def category_detail(request, category_id):
        category = get_object_or_404(Category, pk = category_id)
        return  render(request,'products/category_detail.html', {'category': category}) 

def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

def detail(request, product_id):
        product = get_object_or_404(Product, pk = product_id)
        return  render(request,'products/product_detail.html', {'product': product}) 
