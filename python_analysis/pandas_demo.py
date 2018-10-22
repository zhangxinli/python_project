#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-21 16:05:48
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$

import numpy as np 
import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt 


data = pd.read_csv('D:/workplace/python/2012_Federal_Election_Commission_Database.csv')

# 从info contbr_employer 和 contbr_occupation 有缺失
#缺失的处理

data['contbr_employer'].fillna('NOT PROVIDED',inplace=True)
data['contbr_occupation'].fillna('NOT PROVIDED',inplace=True)

#print('一块有{}为候选人，分别是'.format(len(data['cand_nm'].unique())))
#print(data['cand_nm'].unique())

#得出一块有13位候选人,
#['Bachmann, Michelle' 'Romney, Mitt' 'Obama, Barack'
#"Roemer, Charles E. 'Buddy' III" 'Pawlenty, Timothy' 'Johnson, Gary Earl'
#'Paul, Ron' 'Santorum, Rick' 'Cain, Herman' 'Gingrich, Newt'
#'McCotter, Thaddeus G' 'Huntsman, Jon' 'Perry, Rick']
#
#创建字典，候选人份数那个党派
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

#在data创建一列，加入候选人属于哪个党派
data['party'] =data['cand_nm'].map(parties)
#print(data['party'].value_counts())

#print(data.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[:20])
#
occupation_map = {
  'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
  'INFORMATION REQUESTED':'NOT PROVIDED',
  'SELF' : 'SELF-EMPLOYED',
  'SELF EMPLOYED' : 'SELF-EMPLOYED',
  'C.E.O.':'CEO',
  'LAWYER':'ATTORNEY',
}
def f(x):
	if x in occupation_map:
		return occupation_map.get(x)
	else:
		return x 
#f=lambda x:occupation_map.get(x)
data.contbr_occupation = data.contbr_occupation.map(f)

emp_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'SELF' : 'SELF-EMPLOYED',
   'SELF EMPLOYED' : 'SELF-EMPLOYED',
}
def f1(x):
	if x in emp_mapping:
		return emp_mapping.get(x)
	else:
		return x 
#f1 = lambda x:emp_mapping.get(x)
data.contbr_employer= data.contbr_employer.map(f1)


#处理为负的数据
data=data[data['contb_receipt_amt']>0]




#选取Obama Romney的子数据
data_vs = data[data['cand_nm'].isin(['Obama, Barack','Romney, Mitt'])].copy()

bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])

labels = pd.cut(data_vs['contb_receipt_amt'],bins)
#print(labels)
#
#
#对党派，职业队赞助金额的汇总
print(data['cand_nm'].unique())
by_occupation=data.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='party',aggfunc='sum')
over_2mm=by_occupation[by_occupation.sum(1)>2000000]

#画图
#
#over_2mm.plot(kind='bar')


#求出obama 和romney 出资最高的职业和雇主
# cand_na_grouped=data_vs.groupby(['cand_nm','contbr_occupation'])['contb_receipt_amt'].sum().sort_values(ascending=False)[:7]'
# 一块groupby 是对所有的进行计算
# print(cand_na_grouped)
cand_na_grouped = data_vs.groupby('cand_nm')
def get_top_amt(group,key,n=5):
	grouped =group.groupby(key)['contb_receipt_amt'].sum()
	return grouped.sort_values(ascending=False)[:n]
#print(cand_na_grouped.apply(get_top_amt,'contbr_occupation',7))

# cand_na_grouped = data_vs.groupby('cand_nm')
# def get_top_amount(group,key,n=5):
# 	totals = group.groupby(key)['contb_receipt_amt'].sum()
# 	return totals.sort_values(ascending=False)[:n]
# print(cand_na_grouped.apply(get_top_amount,'contbr_occupation',7))
# 
#对雇主分析
#print(cand_na_grouped.apply(get_top_amt,'contbr_employer',10))


group_bins =data_vs.groupby(['cand_nm',labels])
group_bins_size = group_bins.size().unstack(0)
group_bins_sum =group_bins.sum().unstack(0)

# print(group_bins.size().unstack(0))

# print(group_bins.sum().unstack(0))
#group_bins_sum.plot(kind='bar')


#按照时间
#
print('-------------------')
data_vs['time']=pd.to_datetime(data_vs['contb_receipt_dt'])
print(data_vs.head())