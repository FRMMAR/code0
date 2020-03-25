# _*_ coding: utf-8 _*_
#!/usr/bin/python3

import pdb
import logging
logging.basicConfig(level = logging.INFO) #debug, info, warning. error

def chun(n):
    r = 13/n
    print(r)
    
def __main__():
    try:
        chun(n = 0)
        print('chu over')
    except BaseException as e:
        print('exception happened',":", e)
        logging.info(e)
        pdb.set_trace()
        logging.exception(e)
    print('over')

if __name__ =='__main__':
    __main__()
