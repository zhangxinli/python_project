#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 14:47:17
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$

import pandas as pd
import numpy as np 


url ='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
order_data =pd.read_csv(url,sep='\t')

#前10个
#print(order_data.head(10))


#列表的信息 
# print(order_data.info())

# print(order_data.shape)
# 
#列表的行与列
# print(order_data.columns)
# print(order_data.index)
# 
# 查看最多项目的
# print(order_data.groupby('item_name').sum()['quantity'].sort_values(ascending=False).head(1))
# print(order_data.groupby('item_name').sum().sort_values(['quantity'],ascending=False).head(1))
# 
#同多少个item_name
# print(order_data['item_name'].unique())
# 
# 价格的处理。$去掉
# 
dollar_to_float = lambda x :float(x[1:])
order_data.item_price = order_data.item_price.apply(dollar_to_float)
# print(order_data.head(1))
# 
# 总共买了多少钱

order_data['total_money'] =order_data['quantity']*order_data['item_price']
# print(order_data['total_money'].sum())
# 
# 总共有多少订单
# 
# print(len(order_data['order_id'].unique()))

# print(order_data['order_id'].value_counts())
# 
# 每单的平均价格
order_data.groupby('order_id').sum().mean()['total_money']