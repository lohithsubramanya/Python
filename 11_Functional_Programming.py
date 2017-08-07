### Functional Programming

#lambda

# a = lambda x,y:x*y   ### a - function name , (x*2) - Returns the value after the mentioned operation, x - parameter
# print a('hello',3)


### filters

# a = {2,3,6,8,9,7}

# print filter(lambda x:x%2==0,a)   #### In filter the given logic is always a condition


#### Map  In map the logic is always an operation.

# a = [2,3,6,8,9,7]
# print map(lambda x:x*2, a)


### Reduce  -  In order to reduce a single value out of an entire sequence and get the O/P

# a = [2,3,6,8,9,7]
# print reduce(lambda x,y:x+y,a)



#### comment the entire code and run again in case of infinite loop.