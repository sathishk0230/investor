from background_task import background
import requests as req
import json
import pandas as pd
from datetime import datetime
from dateutil import tz
from .models import equity


@background(schedule=1)
def get_data():
	now = datetime.now()
	india_tz = tz.gettz("Asia/Kolkata")
	now = now.replace(tzinfo = india_tz)
	print('started '+str(now))	
	url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json'
	res=req.get(url)
	j_1=json.loads(res.text)
	#######https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/juniorNiftyStockWatch.json
	url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/juniorNiftyStockWatch.json'
	res=req.get(url)
	j_2=json.loads(res.text)
	url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyMidcap150OnlineStockWatch.json'
	res=req.get(url)
	j_3=json.loads(res.text)
	url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftySmallcap50OnlineStockWatch.json'
	res=req.get(url)
	j_4=json.loads(res.text)
	url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftySmallcap250OnlineStockWatch.json'
	res=req.get(url)
	j_5=json.loads(res.text)
	url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyMidsml400OnlineStockWatch.json'
	res=req.get(url)
	j_6=json.loads(res.text)

	p = pd.DataFrame(j_1['data'])
	p=p.append(j_2['data'])
	p=p.append(j_3['data'])
	p=p.append(j_4['data'])
	p=p.append(j_5['data'])
	p=p.append(j_6['data'])
	nse_data=p.drop_duplicates()

	for eq in equity.objects.all():
	    if eq.symbol in nse_data['symbol'].unique():
	        eq.ltp = float(nse_data.loc[nse_data['symbol']==eq.symbol,'ltP'].values[0].replace(',',''))
	        eq.y_h = float(nse_data.loc[nse_data['symbol']==eq.symbol,'wkhi'].values[0].replace(',',''))
	        eq.y_l = float(nse_data.loc[nse_data['symbol']==eq.symbol,'wklo'].values[0].replace(',',''))            
	        if eq.buy_watch_price==0.0:
	            eq.buy_per_change= 0.0
	        else:
	            eq.buy_per_change = ((eq.ltp-eq.buy_watch_price)/eq.buy_watch_price)*100
	        if eq.sell_watch_price==0.0:
	            eq.sell_per_change= 0.0
	        else:
	            eq.sell_per_change = ((eq.ltp-eq.sell_watch_price)/eq.sell_watch_price)*100
	        eq.save()
	    else:
	    	eq.ltp=-1
	    	eq.save()
	print('end')
	#return now