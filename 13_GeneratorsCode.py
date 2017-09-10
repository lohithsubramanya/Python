'''
def func():
    i = 0
    while True:
        return i
        i += 1

#func returns generator object
#f = func()
print func()
print func()
#print d.next()
#function calls are stateless, the prev value of variables is not known



def func():
    i = 0
    while True:
        if i%2 == 0:
            yield i*2
        else:
            yield i*3
        i += 1

f = func()
print type(f)
#Call next() function with genrator to execute the function once

print f.next()
print f.next() 
print f.next()
print f.next() 


 
f = itertools.combinations([1,2,3,5,6],2)

while True:
    try:
        print f.next()
    except:
        break
'''

###Decorators
#f -> this is the function on which the decorator was annotated
#The decorator function returns a function which will be excuted in place of the actual function call

def my_new_work(f):

    #Function inside function - inner function
    def new_behavior(num):
        if num > 2:
            f(num)
        print 'My New Hello World'
    #return the inner function, this is the func which gets executed
    return new_behavior

@my_new_work
def func(num):
    print "hello World"

#Uses of decorators
#1. Adding security
#2. 

func(10)