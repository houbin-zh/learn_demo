#-*-coding:utf-8-*-

import time,threading

balance = 0
lock = threading.Lock()

def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n<5:
		n += 1
		print('thread %s >>> %s' %(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

#多线程中，所有变量被线程共用，线程锁可以保证某段代码被一个线程完整执行
def change_balance(n):
	global balance

	lock.acquire()  #获取锁
	try:
		balance += n
		balance -= n  #确保修改balance的代码被一个线程完整执行
	finally:
		lock.release()  #释放锁

def run_thr(n):
	for i in range(10000000):
		# lock.acquire()
		# try:
		# 	change_balance(n)
		# finally:
		# 	lock.release()
		change_balance(n)

def creatThr():
	print('thread %s is running...' % threading.current_thread().name)
	thr1 = threading.Thread(target=loop,name='LoopThread')
	#thr1.start()
	#thr1.join()

	thr2 = threading.Thread(target=run_thr,args=(5,))
	thr3 = threading.Thread(target=run_thr,args=(8,))
	thr2.start()
	thr3.start()
	thr2.join()
	thr3.join()
	print('thread %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
	creatThr()
	print('balance:',balance)
