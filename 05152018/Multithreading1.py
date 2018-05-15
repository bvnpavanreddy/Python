
"""import queue
import threading
import time


exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
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
            print('%s procession %s'%(threadName,data))
        else:
            queueLock.ralease()
            time.sleep(1)

threadList=['Thread-1','Thread-2','Thread-3']
nameList=['one','two','three','four','five']
queueLock=threading.Lock()
workQueue=queue.Queue(10)

threads=[]
threadID=1


for tName in threadList:
    thread=myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID +=1


queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print('exiting main thread')"""



"""import multiprocessing

def cal_squares(numbers,q):
    for n in numbers:
        q.put(n*n)


if __name__ == '__main__':
    numbers = [22,33,44]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_squares,args=(numbers,q))

    p.start()
    p.join()


    while q.empty() is False:
        print(q.get())"""



"""import time
import multiprocessing

def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1

def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1


if __name__ == '__main__':

    balance = multiprocessing.Value('i',200)
    d = multiprocessing.Process(target=deposit,args=(balance,))
    w = multiprocessing.Process(target=withdraw,args=(balance,))

    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)"""



"""import time
import multiprocessing

def deposit(balance):
    for i in rance(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value +1
        lock.release()

def withdraw(balance):
    for i in rance(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit,args=(balance,))
    w = multiprocessing.Process(target=withdraw,args=(balance,))

    d. start()
    w.start()
    d.join()
    w.join()
    print(balance.value)"""


"""from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == '__main__':
    array = [1,2,3,4,5]
    p = Pool()
    result = p.map(f,array)
    print(result)"""

from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1=time.time()
    p=Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join()

    print('pool took:',time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))
    print('series processiong took :',time.time()-t2)

    






