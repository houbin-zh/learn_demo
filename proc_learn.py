#-*-coding:utf-8-*-

from multiprocessing import Process,Pool
import os,time,random,subprocess

def run_proc(name):
	print('child processing %s(%s) is running...' %(name,os.getpid()))

def creatChildProc():
	print('parent processing %s is running...' %(os.getpid()))
	p = Process(target=run_proc,args=('test',))  #Process()创建子进程，传入执行的函数和参数
	print('child processing will start')
	p.start()
	p.join()  #等待子进程结束后再往下进行，常用于进程间的同步
	print('child processing end')

def long_time_task(name):
	print('child processing %s(%s) is running...' %(name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*10)  #random()产生[0,1)的随机数
	end = time.time()
	print('child processing %s(%s) run %s s.' %(name,os.getpid(),(end-start)))

def creatProcPool():
	print('parent processing %s is running...' %(os.getpid()))
	p = Pool(4)  #能同时执行的最大进程数
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('processing pool will start')  #主进程在运行时，碰到了子进程，需要等到操作系统切换进程时，再交给子进程，所以这行仍在运行
	p.close()
	p.join()  #等待进程池结束后再向下进行，若不这样，主进程会继续向下运行，可能在切换进程前主程序已结束
	print('processing pool end')

if __name__ == '__main__':
	#creatChildProc()
	creatProcPool()
