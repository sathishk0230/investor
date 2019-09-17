from django.http import HttpResponse
from django.shortcuts import render
from .models import equity,derivative
from django.db.models import Q
#repeating background tasks
from .tasks import get_data

#for webscrapping
import requests as req
import json
import pandas as pd
def edit_wp(request):
    try:
        symbol = request.GET.get("symbol")
        buy_wp = request.GET.get("buy_wp")
        sell_wp = request.GET.get("sell_wp")
        e = equity.objects.filter(symbol=symbol)[0]
        if buy_wp:
            e.buy_watch_price = buy_wp
        if sell_wp:
            e.sell_watch_price = sell_wp
        e.save()

        get_data()
        equity_set = equity.objects.all()
        not_updated = equity_set.filter(ltp = -1)
        equity_set = equity_set.filter(~Q(ltp = -1))
        pinned_obj = equity.objects.filter(pinned=True)
        unpinned_obj = equity.objects.filter(pinned=False)
        
        context = {'pinned_equitys':pinned_obj,'unpinned_equitys':unpinned_obj,'not_updated':not_updated}
    
    except  IndexError:
        raise(Exception("Symbol entered was not found."))
    except ConnectionError:
        raise(Exception("NET connection problem."))
    return render(request , 'watcher/index1.html',context)

def index(request):
    to_pin = request.GET.get('pin')
    order = request.GET.get('order')
    if to_pin:
        obj_set = equity.objects.filter(symbol=to_pin)
        for obj in obj_set:
            obj.pinned = not(obj.pinned)
            obj.save()

    get_data()

    if order=="bpc":
        equity_set = equity.objects.all().order_by("buy_per_change")
    elif order=="-bpc":
        equity_set = equity.objects.all().order_by("-buy_per_change")
    elif order=="spc":
        equity_set = equity.objects.all().order_by("sell_per_change")
    elif order=="-spc":
        equity_set = equity.objects.all().order_by("-sell_per_change")
    elif order=="a":
        equity_set = equity.objects.all().order_by("symbol")
    elif order=="-a":
        equity_set = equity.objects.all().order_by("-symbol")
    else:
        equity_set = equity.objects.all().order_by("symbol")
    
    not_updated = equity_set.filter(ltp = -1)
    equity_set = equity_set.filter(~Q(ltp = -1))
    pinned_obj = equity_set.filter(pinned=True)
    unpinned_obj = equity_set.filter(pinned=False)
    
    context = {'pinned_equitys':pinned_obj,'unpinned_equitys':unpinned_obj,'not_updated':not_updated}
    return render(request , 'watcher/index1.html',context)

def detail(request , symbol="symbol"):
    context = {
    'symbol' : symbol
    }
    return render(request,'watcher/detail.html' , context )