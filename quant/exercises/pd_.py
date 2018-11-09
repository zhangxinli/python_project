#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 14:21:46
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$

import tushare as ts
import pandas as pd 
import numpy as np 
from datetime import date 
import matplotlib.pyplot as plt
import matplotlib.finance as mpf 


def init_ts():
	pro = ts.pro_api()
	ts.set_token('dfe14fff018861ab3ba1aa7da8ce5b9df943ac285a7c7b55fb3c064f')
	return pro



def get_daily(code,start='20080101',end=date.today().strftime('%Y%m%d')):
	pro = init_ts()
	return ts.pro_bar(pro_api=pro, ts_code=code,start_date=start, end_date=end)


data = get_daily('000001.SZ')
data =data.set_index('trade_date')
# data[['close','vol']].plot(subplots=True,style=['r','g'],grid=True)
# plt.show()
# 

# random_data =np.random.random((300,500))
# index_cols = ['股票'+str(i) for i in range(random_data.shape[0])]
# days = pd.date_range('2017-01-01',periods=random_data.shape[1],freq='1d')
# df =pd.DataFrame(random_data,index=index_cols,columns=days)
# df2 = df.T.resample('3D').mean()
# print(df2)
# changes = pd.qcut(data.change,10)
# print(changes.value_counts())

# dates =pd.to_datetime(data.index)
# def get_weekday(s):
# 	return s.weekday()+1
# data['week'] = dates.map(get_weekday)

# #交叉表
# data['positive'] = np.where(data['change']>0,1,0)
# xt = pd.crosstab(data['week'],data['positive'] )
# 
# 
# 跳空
# 
# data['preClose'] = data['close'].shift(1)
# print(data[['close','preClose']].head(10))
jump_threshold = data.close.median()*0.03


# print(data.change.head(10))
jump_pd = pd.DataFrame()

def judge_jump(day):
	
	global jump_pd
	if day.change > 0  and (day.low - day.pre_close)>jump_threshold:
		day['jump'] = 1 
		day['jump_power'] =(day.low - day.pre_close)/jump_threshold
		jump_pd.append(day)
	elif day.change < 0  and (day.low - day.pre_close)<jump_threshold:
		day['jump'] = -1 
		day['jump_power'] =(day.pre_close - day.high)/jump_threshold
		jump_pd.append(day)

# for k_index in np.arange(0,data.shape[0]):
# 	judge_jump(data.iloc[k_index])
# data.apply(judge_jump,axis=1)

# print(jump_pd.filter(['jump','jump_power','change']))

data_part = data[:30]
fig,ax = plt.subplots(figsize=(14,7))
qutotes=[]

for index ,(d,o,c,h,l) in enumerate(zip(data_part.index,data_part.open,data_part.close,data_part.high,data_part.low)):
	d = mdf.date2num(d)
	val=(d,o,c,h,l)
	qutotes.append(val)
mdf.candlestick_ochl(ax,qutotes,width=0.6)
ax.autoscale_view()
ax.xaxis_date()
plt.show()







