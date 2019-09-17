from . import views
from django.conf.urls import url

app_name = 'orderbook'
urlpatterns = [
    url(r'^$', views.index , name = 'index'),
]