# while , for 

# a = 5

# while a < 10: 
# 	print a
# 	a+=2

# a = 10 
# while a > 0:
# 	a-=2
# 	print a



# a = 13 
# while a > 2:
# 	if a%5 == 0:
# 		print a
# 	a-=1


## for loop 

# for var in range(1,100,3):
# 	print var

# for i in 'hello':
# 	print i


# s = 'this is a string'
# for a in s:
# 	if a == 'a' or a == 'i' or a == 'e' or a == 'o' or a =='u':    #### OR if i in 'aeiou':
# 		print a


# s = 'this is a string'
# sum = 0
# for a in s:
# 	if a == 'a' or a == 'i' or a == 'e' or a == 'o' or a =='u':
# 		sum +=1
# print sum


# for i in range(1,21):
# 	if i%5 == 0:
# 		print i


# for i in range(1,6):
# 	for j in range(1,11):
# 		print i, 'x', j, '=' , i*j



# s = 'hello'

# for i in s: 
# 	if i == 'l':
# 		break      ## breaks the loop and doesnt go inside else loop
# 	else: 
# 		print i
# print 'outside the loop'



# s = 'hello'

# for i in s: 
# 	if i == 'l':
# 		continue      ## skips the iteration and goes back to line 70 without touching line 75
# 	else: 
# 		print i
# 	print "outside if else"
# print 'outside the loop'



# s = 'hello'

# for i in s: 
# 	if i == 'l':
# 		pass     ## skips only the operation for specified condition and goes to line 87
# 	else: 
# 		print i           ### Here, it skips the else loop
# 	print'outside if but inside for' 
# print 'outside the loop'



#### 1 

# for i in range (1500,2701):
# 	if i%5 == 0 and i%7 == 0:
# 		print i 



#### 3 


# Even = 0
# Odd = 0

# for n in range(1,10):
# 	if n%2 == 0:
# 		Even+=1
# 	else:
# 		Odd+=1
# print 'Even count =',Even 
# print 'Odd count =',Odd



##  7 

# for i in range(1,51):
# 	if i%3 == 0 and i%5 == 0:
# 		print"FizzBuzz"
# 	elif i%3 == 0:
# 		print"Fizz"
# 	elif i%5 == 0:
# 		print"Buzz"
# 	else:
# 		print i




## 8 

# Sum = 0
# Count = 0

# for i in range(-4567, 9275628):
# 	Sum+=i
# 	Count+=1
# print 'Sum is', Sum

# Average = Sum/Count
# print "Average is", Average




## 10 

# x = 'abcd'
# for i in range(len(x)):
# 	x = 'a'
# 	print(x)



## 9 - Fibonacci series

# a = 0
# b = 1	
# while a < 50:
# 	print a,
# 	a,b = b,a+b
