import threading
def myfunc1():
  return 1+2
def myfunc2():
  return 3+4
t1=threading.Thread(target=myfunc1)
t2=threading.Thread(target=myfunc2)
t1.start()
t1.join()
t2.start()
t2.join()
