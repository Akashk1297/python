from multiprocessing import Process
def func1():
  return 1+2
p1=Process(target=myfunc1)
p1.start()
p1.join()
