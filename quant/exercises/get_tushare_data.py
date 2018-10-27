#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 20:59:50
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$
from sqlalchemy import create_engine
import tushare as ts
from datetime import date 
from sqlalchemy.types import VARCHAR


#查询当前所有正常上市交易的股票列表
#dfe14fff018861ab3ba1aa7da8ce5b9df943ac285a7c7b55fb3c064f


#初始化
def init_ts():
	pro = ts.pro_api()
	ts.set_token('dfe14fff018861ab3ba1aa7da8ce5b9df943ac285a7c7b55fb3c064f')
	return pro


def init_mysql():
	engine =create_engine('mysql+pymysql://root:zxlzxl123@127.0.0.1/stocks?charset=utf8')
	return engine


#保存到数据库，前提表不存在
def to_mysql(data,table_name):
	engine =init_mysql()
	if type(data.index).__name__ =='RangeIndex':
		
		data.to_sql(table_name,engine,if_exists='append')
	else:
		index_name=data.index.names
		dict_dtype={}
		for i in range(len(index_name)):
			dict_dtype[index_name[i]] =VARCHAR(data.index.get_level_values(index_name[i]).str.len().max())
		
		data.to_sql(table_name,engine,if_exists='append',index_label=data.index.names,dtype=dict_dtype)
	
	
	

#把获取tushare的symble
def get_symble():
	pro=init_ts()
	data = pro.stock_basic(exchange_id='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date,is_hs')
	return data


#获取交易日期
def get_trade_cal(start='19900101',end=date.today().strftime('%Y%m%d')):
	pro=init_ts()
	return pro.query('trade_cal', start_date=start, end_date=end)



def get_company():
	pro =init_ts()
	return pro.stock_company()

# 获取沪深股通的成分股
# SH ,SZ
def get_hs_const(type='SH'):
	pro = init_ts()
	return pro.hs_const(hs_type=type)




#获取每日行情

def get_daily(code,start='20080101',end=date.today().strftime('%Y%m%d'),ma=[5,10,20]):
	pro = init_ts()
	return ts.pro_bar(pro_api=pro, ts_code=code,start_date=start, end_date=end)


def daily_to_sql():
	symbols=get_symble()
	for i in range(len(symbols)):
		data = get_daily(symbols.ix[i,'ts_code'])
		data =data.set_index(['trade_date','ts_code'])
		# print(data)
		to_mysql(data,'daily_price')



