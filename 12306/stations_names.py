#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-29 23:30:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re
import requests
import json



url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9069'
reponse =requests.get(url)
if reponse.status_code == 200:
	action_str =re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',reponse.text)
	if action_str:
		action_name =json.dumps(dict(action_str),ensure_ascii=False)
		str ="stations="+action_name
		write =open("stations.py",'w',encoding='utf-8')
		write.write(str)
		write.close()




