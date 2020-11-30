import threading

class SummingThread(threading.Thread):
     def __init__(self,min,max):
         super(SummingThread, self).__init__()
         self.min=min
         self.max=max


     def run(self):
         while self.max>self.min :
             self.max-=1


thread1 = SummingThread(0,1E7/2)
thread2 = SummingThread(0,1E7/2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
result = thread1.max + thread2.max
print (result)