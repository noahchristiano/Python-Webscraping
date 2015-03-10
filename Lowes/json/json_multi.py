# json_multi.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

from multiprocessing import Process
from Queue import Queue
from lowes_json import LowesJson

job_q = Queue()
result_q = Queue()

def file_contains(num):
	file = open('test.txt')
	duplicate = False
	for line in file:
		if line == num + '\n':
			print 'Found duplicate: ' + num
			duplicate = True
	file.close()
	return duplicate

def write(results):
	for r in results:
		if not file_contains(r):
			file = open('test.txt', 'a')
			print 'Writing store: ' + r
			file.write(r + '\n')
			file.close()

def writer():
	while True:
		if not result_q.empty():
			s = result_q.get()
			if s != None:
				write(s)

def run(id):
	while True:
		collector = LowesJson()
		num = job_q.get()
		print 'Process ' + str(id) + ' getting place: ' + "%05d" % num
		s = collector.get_stores(num)
		if s != None:
			result_q.put(s)
		job_q.task_done()

if __name__ == '__main__':
	print 'Populating job queue ...'
	for i in range(500, 100000):
		job_q.put(i)

	print 'Starting writer process ...'
	e = Process(target=writer)
	e.start()

	print 'Starting worker processes ...'
	for i in range(7):
		p = Process(target=run, args=(i + 1,))
		p.start()
		print 'Started process: ' + i
