#-*-coding:utf-8-*-

import re
from datetime import datetime,timedelta,timezone

def dt_test():
	#获取当前时间
	now = datetime.now()
	print("当前时间为：",now)

	#获取指定时间，传入参数
	dt = datetime(2018,1,1,12,30,50)
	print("指定一个时间为：",dt)

	#计算机存储当前时间用timestamp，timestamp值与时区无关
	ts = now.timestamp()
	print("当前时间的timestamp值为：",ts)
	#小数位表示毫秒

	#将timestamp转换为时间
	time = datetime.fromtimestamp(ts)
	print("timestamp转换为时间：",time) #本地时间

	utctime = datetime.utcfromtimestamp(ts)
	print("timestamp转换为UTC标准时区时间：",utctime) #UTC时间

	#string和datetime的转换
	cday = datetime.strptime('2018-1-2 02:50:30','%Y-%m-%d %H:%M:%S')
	print("2018-1-2 02:50:30转换为datetime：",cday)

	strtime = now.strftime('%a,%b,%d %H:%M')
	print("当前时间转换为string：",strtime)

	plustime = now + timedelta(days=2,hours=4)
	print("当前时间往后2天4小时：",plustime)

	subtime = now - timedelta(hours=5)
	print("当前时间往前5小时",subtime)

	#转换时区,tzinfo为时区信息
	utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) #强制设置时区
	print("UTC时间为：",utc_dt)
	bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
	print("UTC时间转换为北京时间：",bj_dt)
	tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
	print("UTC时间转换为东京时间：",tokyo_dt)
	#创建时区
	utc_8 = timezone(timedelta(hours=8))
	bj_dt = datetime.now().replace(tzinfo=utc_8)
	print("UTC8时间：",bj_dt)

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
def to_timestamp(str1,str2):
	dt = datetime.strptime(str1,'%Y-%m-%d %H:%M:%S')
	if re.match(r'\b[a-zA-Z]{3}\+\d{1}\:\d{2}',str2):
		a,b,c,_,n,*other = str2
		n = int(n)
		utc_n = timezone(timedelta(hours=n))
	else:
		print("时区信息有误！")

	dt = dt.replace(tzinfo=utc_n)
	ts = dt.timestamp()
	print("输入的string转换为timest：",ts)

#dt_test()
to_timestamp('2018-1-1 17:18:30','UTC+5:00')
