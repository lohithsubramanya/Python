### functions 

# def func():
# 	print 'this is function'

# func() ### Always call the function after building it.

# def sumFunc(a,b):  #### a,b  -  Parameters
# 	a=5
# 	b=3
# 	c=a+b
# 	print c   ###  Works best internal to the function
# 	return c  ### Is used to get the output value outside the function

# sumFunc(3,4)  #### 3,4 - Arguments

##### Required arguments

# def fun(m,n):   ### Default argument is declared when we assign a value to an argument, It should always be declared starting from the end of paranthesis.
# 	print m
# 	print n

# fun(3,5)  #### No. Arguments should always be equal to no. of parameters


### Keyword Arguments


# def fun(m,n,a,b): 
# 	print m
# 	print n
# 	print a
# 	print b

# fun(a=5,b=6,m=2,n=1) ##### To pass a value without assignment it should start from the 1st parameter of the calling function


#### Variable length argument

# def fun(m,*n):   ### Boxing
# 	print m
# 	print n 

# fun(3,5,7,34,2,6) ### First value is given to 'm' and the remaining values are converted to a tuple and stored in n


# def fun(m,n,a,b):   ### Unboxing  - We cannot pass a dictionary here
# 	print m
# 	print n
# 	print a
# 	print b 

# d = [2,4]   #### Values 2 and 4 are assigned to a and b
# fun(3,4,*d) ### First value is given to 'm' , 2nd to n. 


# def fun(m,n,a,b):   ### Unboxing  - We can pass a dictionary here
# 	print m
# 	print n
# 	print a
# 	print b 

# d = {'a':2,'b':4}   #### Values 2 and 4 are assigned to a and b
# fun(3,4,**d) ### First value is given to 'm' , 2nd to n. 


# def fun(m,**n):   ### Boxing for dictionary
# 	print m
# 	print n 

# fun(3,a=2,b=4,c=1) ### First value is given to 'm' , 2nd to n. 