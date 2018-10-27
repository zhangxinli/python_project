#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 17:32:41
# @Author  : xinli (xinli.zxl@foxmail.com)
# @Link    : 
# @Version : $Id$
# 
# 
# 



from bs4 import BeautifulSoup
import requests
from datetime import datetime


def obtain_wiki_snp500():
	"""
	# 从维基获取股票的符号
	"""
	now = datetime.utcnow()
	response =requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup =BeautifulSoup(response.text)
	symbol_lists =soup.select('table')[0].select('tr')[1:]
	symbols=[]
	for symbol_list in symbol_lists:
		tds = symbol_list.select('td')
		symbols.append((
			tds[0].select('a')[0].text,
			'stock',
			tds[1].select('a')[0].text,
			tds[3].text,
			'USD',now,now

			))
	print(symbols)
	return symbols



obtain_wiki_snp500()
