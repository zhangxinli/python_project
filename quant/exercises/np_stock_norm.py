#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 13:40:58
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


stock_day = np.random.standard_normal((200,500))

# stock_0_mean = stock_day[0].mean()
# stock_0_std =stock_day[0].std()

# plt.hist(stock_day[0],bins=50,normed=True)

# fit = np.linspace(stock_day[0].min(),stock_day[0].max())

# pdf = stats.norm(stock_0_mean,stock_0_std).pdf(fit)

# plt.plot(fit,pdf,lw=2,c='r')

# plt.show()
# 
# 正态分布买入
# 
print(np.argsort(np.sum(stock_day,axis=1))[:3])




