#coding: utf-8
import multiprocessing
import time

def func(msg):
    print ("msg:", msg)
    time.sleep(3)
    print ("end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 5)   #the number of processes
    for i in range(10):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))   
    print ("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   # first close to avoid the change of pool, then join 
    print ("Sub-process(es) done.")
