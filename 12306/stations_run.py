# coding:utf-8

"""命令行火车票查看器
Usage:
	tickets [-gdtkz] <from> <to> <date>
"""

from stations import stations
import requests
import prettytable as pt

import sys



class Trains(object):

	def __init__(self,header,data):
		self.header =header
		self.data = data

	def draw(self):
		tb = pt.PrettyTable()

		tb.field_names = self.header

		for i in range(len(self.data)):

			tb.add_row(self.data[i])
		print(tb)







def init():
	from_station= stations[sys.argv[1]]
	to_station= stations[sys.argv[2]]
	date =sys.argv[3]
	url ='https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
	response =requests.get(url, verify=False)
	print(response.status_code)
	if response.status_code != 200 :
		return

	try:
		response.json()
	except BaseException:
		print("无数据")
		return

	maps =response.json()['data']['map']
	result =response.json()['data']['result']

	header = "|车次|起点|终点|发车时间|到达时间|用时|是否当天|商务座|一等座|二等座|高级软卧|软卧|动卧|硬座|软座|无座|其他".split("|")

	datas = []
	for i in range(len(result)):
		details = result[i].split("|")
		data =[]

		data.append(details[3])
		if details[4] in maps.keys():
			data.append(maps[details[4]])

		else:
			data.append(sys.argv[1])


		if  details[5] in maps.keys():
			data.append(maps[details[5]])

		else:
			data.append(sys.argv[2])


		data.append(details[8])
		data.append(details[9])
		data.append(details[10])
		data.append(details[11])

		data.append(details[30])
		data.append(details[31])
		data.append(details[32])

		data.append(details[21])
		data.append(details[23])

		data.append(details[33])
		data.append(details[28])
		data.append(details[29])
		data.append(details[25])
		data.append(details[26])

		data.append(details[27])
		datas.append(data)

	Trains(header,datas).draw()

if __name__ == '__main__':
    init()










