# -*-coding=utf-8-*-
'''
装饰器例子
针对斐波那契数列和爬楼问题的应用
装饰器作为缓存，对结果进行查询，消除递归的重复运算
'''
import time

def decorator(func):
	cache = {}   #缓存dict
	def wrap(*args):  #可变参数，适应多参数的函数
		if args not in cache:  #查询dict，注意dict的key为args，args必须为hashable
			#print("%s is running..."%func.__name__)
			cache[args] = func(*args)
		return cache[args]
	return wrap

def log(func):
	def wrap(*args):
		print("%s is running..."%func.__name__)
		return func(*args)
	return wrap

'''
装饰器在不影响原函数功能的情况下，可为原函数增加某功能
将原函数作为装饰器的参数
注意原函数参数和装饰器参数
'''

@decorator
def fib(n):
	if n==0 or n==1:
		return 1
	else:
		return fib(n-2)+fib(n-1)

@decorator
def climb(n,steps):
	count = 0
	if n<=1:
		count = 1
	else:
		for step in steps:
			count += climb(n-step,steps)
	return count

start = time.time()
#print([fib(n) for n in range(10)])
print(climb(100,(1,2,3,4))) #(1,2,3,4)用tuple而不是list，此参数会作为装饰器中cache[]的key，必须为hashable
end = time.time()
print("cost time:",end-start)
 