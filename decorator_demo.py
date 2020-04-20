# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:50:18 2020

@author: 1
"""
## part 1
print("## part 1")
# function == variable
def hi(name="hard-working u"):
    return "hi " + name
 
print(hi())
# call a function 

greet = hi
# use function name as a variable
 
print(greet())
# call a function by this variable
 
del hi
 
print(greet())
# outputs: 'hi yasoob'


## part 2
print("## part 2")
# define funcion inside function
# function cannot called in outside
def hi(name = "FinsideF"):
    print("hi" + name)
    
    def a1():
        print("hia1" + name)
        
    def a2():
        print("hia2" + name)
        
hi()

## part 3
print("## part 3")
# return a function
def hi(name="work so hard"):
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    if name == "work so hard":
        return greet
    else:
        return welcome
 
a = hi()
print(a)
print(a())

## part 4
print("## part 4")
# use function as parameters
def hi():
    return "hi u bravo!"
 
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())
 
doSomethingBeforeHi(hi)

## part 5
print("## part 5")
# the original of the decorator
# inner function inside of the outer function
# outer function return inner function
def a_new_decorator(a_func):
 
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction
 
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
 
a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"
 
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()
 
a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()

## part 6
print("## part 6")
# Syntactic sugar
# the usage of @ symbol
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")
 
a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()
 
#the @a_new_decorator is just a short way of saying: a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

## part 7
print("## part 7")
# solve the problem of a_function_requiring_decoration.__name__ == wrapTheFunction
# by using functools.wraps(func) inside of the decorator

from functools import wraps
 
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction
 
@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")
 
print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration

      
## part 8
print("## part 8")
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
 
@decorator_name
def func():
    return("Function is running")
 
can_run = True
print(func())
# Output: Function is running
 
can_run = False
print(func())
# Output: Function will not run
      
## part 9
print("## part 9 authorization")
# flask & Django
from functools import wraps
 
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated




## part 10
print("## part 10 logging")
from functools import wraps
 
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
 
@logit
def addition_func(x):
   """Do some math."""
   return x + x
 
 
result = addition_func(4)
# Output: addition_func was called

## part 11
print("## part 11 decorator with parameters")
from functools import wraps
 
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator
 
@logit()
def myfunc1():
    pass
 
myfunc1()
# Output: myfunc1 was called
# output to out.log
 
@logit(logfile='func2.log')
def myfunc2():
    pass
 
myfunc2()
# Output: myfunc2 was called
# output to func2.log

## part 12
print("## part 12 decorator with parameters")

from functools import wraps
 
class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile
 
    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # write content to logfile
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            # send a notice
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function
 
    def notify(self):
        # only log
        pass

@logit()
def myfunc1():
    pass


## part 12
print("## part 12 decorator with parameters")
class email_logit(logit):
    '''
    call the function, at the same time, email it
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)
 
    def notify(self):
        # send an email to self.email
        pass



