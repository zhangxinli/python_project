#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 19:09:29
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$

import pandas as pd
import numpy as np 


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

data = pd.read_table(url,sep='|',index_col='user_id')

#
#查看数据user_id
# print(data.head(1))
# print(data.shape)
# print(data.info())
# 
# 职业最多的
# print(data['occupation'].value_counts().head(10))
# 
# 
# print(data.describe(include='all'))