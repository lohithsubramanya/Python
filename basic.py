#### Write a Python program to get the Python version you are using.

# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)



#### Write a Python program to display the current date and time.

# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


#### Write a Python program which accepts the radius of a circle from the user and compute the area.

# from math import pi
# # r = float(input ("Input the radius of the circle : "))
# r = 5.7
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#### Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# a = 7
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)


### Program to print the calendar given year and month

# import calendar
# y = 2017
# m = 3
# print(calendar.month(y, m))


#### Python program to calculate number of days between two dates

# from datetime import date

# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# d = l_date - f_date
# print(d.days)


#### Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.


# def difference(n):
#     if n <= 17:
#         return (17 - n)
#     else:
#         return (n - 17) * 2 

# print(difference(22))
# print(difference(14))


#### Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str

# print(new_string("Array"))
# print(new_string("IsEmpty"))


#### Python program to get a string which is n (non-negative integer) copies of a given string.


# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result

# print(larger_string('abc', 12))
# print(larger_string('.py', 3))


#### Program to check whether a specified value is contained in a group of values

# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#     return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))


#### Program to create a histogram from a given list of integers

# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '$'
#           times = times - 1
#         print(output)

# histogram([2, 3, 6, 5])



####  Program to compute the greatest common divisor (GCD) of two positive integers

# def gcd(x, y):
#     gcd = 1
    
#     if x % y == 0:
#         return y
    
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break  
#     return gcd

# print(gcd(12, 17))
# print(gcd(4, 6))


