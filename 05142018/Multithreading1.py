"""import time
import threading

def cal_squares(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.3)
        print('square:',n*n)


def cal_cubes(numbers):
    print('calculate cube of numbers')
    for n in numbers:
        time.sleep(0.5)
        print('cube:',n*n*n)


arr=[2,5,8,9]

t=time.time()
t1=threading.Thread(target=cal_squares,args=(arr,))
t2=threading.Thread(target=cal_cubes,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print ('done in :',time.time()-t)"""





"""import time
import multiprocessing
squares_results=[]

def cal_square(numbers):
    global squares_results
    for n in numbers:
        print('squares:'  ,str(n*n))
        squares_results.append(n*n)
        print('with in a process :result'+ str(squares_results))

#def cal_cubes(numbers):
  #  for n in numbers:
    #    print('cubes:',  str(n*n*n))

if __name__ == '__main__':

    arr=[12,23,58,66]

    p1=multiprocessing.Process(target=cal_square,args=(arr,))
    #p2=multiprocessing.Process(target=cal_cubes,args=(arr,))

    p1.start()
    #p2.start()

    p1.join()
    #p2.join()

    print('done!')"""


"""import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count <5:
        time.sleep(delay)
        count +=1
        print('%s:%s'%(threadName,time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,('Thread-1',2,))
    _thread.start_new_thread(print_time,('Thread-2',4,))

except:
    print('Error:unable to start thread')


while 1:
    pass"""



"""import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID= threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('starting', self.name)
        print_time(self.name,self.counter,5)
        print('existing ',self.name)


def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            theradName.exit()
        time.sleep(delay)
        print('%s:%s' %(threadName,time.ctime(time.time())))
        counter-=1

thread1=myThread(1,'Thread-1',1)
thread2=myThread(2,'Thread-2',2)


thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('exiting main thread')"""



"""import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter = counter

    def run(self):
        print('starting',self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print('%s:%s'%(threadName,time.ctime(time.time())))
        counter -=1

threadLock=threading.Lock()
threads=[]

thread1=myThread(1,'Thread-1',1)
thread2=myThread(2,'Thread-2',2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print('exiting main Thread')"""


import queue
import threading
import time


exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__inti__(self)
        self.threadID=threadID
        self.name=name
        self.q=q

    def run(self):
        print('starting',self.name)
        process_data(self.name,self.q)
        print('exiting',self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print('%s procession %s'%(threadNmae,data))
        else:
            queueLock.ralease()
            time.sleep(1)

threadList=['Thread-1','Thread-2','Thread-3']
nameList=['one','two','three','four','five']
queueLock=threading.Lock()
workQueue=queue.Queue(10)

threads=[]
threadID=1


for tNmae in threadList:
    thread=myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1


queueLock.acquire()
for word in nameList:
    workQueue.pu(word)
queueLock.release()

while not workQueue.empty():



