# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:34:09 2020

@author: 1
"""

import sys

def test():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Hello,sys.argv is %s!' % args)

if __name__=='__main__':
    test()