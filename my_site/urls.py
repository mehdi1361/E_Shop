from django.conf.urls import url
from products import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^category/$', views.category_list, name='category_list'),
        url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^showdate', views.current_datetime, name='show_date'), ]
