from . import views
from django.conf.urls import url

app_name = 'watcher'

urlpatterns = [
	#/watcher/
    url(r'^$', views.index , name = 'index'),
    #/watcher/somesymbol/
    url(r"^(?P<symbol>([a-z|0-9|A-Z|\-|&]+))/$" ,views.detail ,name = 'detail'),
    #/watcher/somesymbol/
    #url(r"^(?P<symbol>([a-z|0-9|A-Z]+))/$" ,views.detail ,name = 'detail'),

    #/watcher/edit_wp/?symbol=!!&wp=!!
    url(r"^edit_wp/$", views.edit_wp ,name = "edit_wp"),
]