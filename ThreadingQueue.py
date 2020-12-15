import threading

class ThreadingQueue:
    # use list, the semaphores will block enqueue and dequeue if empty or full
    def __init__(self):
        self.queue = [] # initialize queue
        self.empty = threading.Semaphore(10) # semaphore capacity
        self.full = threading.Semaphore(0) # wait until other thread calls release
        self.lock = threading.Lock()
    
    # full and empty used to track capacity
    def enqueue(self,item):
        self.empty.acquire()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.full.release() # if capacity of 10 aquired, wait until consumer releases

    def dequeue(self):
        self.full.acquire()
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        self.empty.release() # release permit that we used to add a frame to the first queue
        return item
