### Exceptions  - Predefined
 
### Almost 15 exceptions declared by python itself.
# try:                  ##### Nested try , except is also valid 
# 	print b
# except NameError:
# # 	b=0
# # 	print b, 'this error occured due to name error'
# # except IOError:
# # 	print 'error'

# else:                               #### Else and finally are optional things as part of try except.
# 	print 'No error'
# finally:
# 	print 'finally'  ### Executes irrespective of exception occurance or not.


#### Regular Expression

###  . Means Any character 
###  ^ Beginning of the string
###  $ End of the string
###  * Zero or more repititions of the preceding pattern
###  + One or more repititions of the preceding pattern
###  ? zero or one repititions of the preceding pattern
###  {m} Means any integer  Eg : a{6} - This means 'aaaaaa'
###  {m,n} Eg : a{3,5} - This means 'aaa' or 'aaaa' or 'aaaaa'
###  '|' Means Logical OR
###   \s  Means space
###   \d  Means digit
###   \w  Means alphanumeric characters

### In order to use any of the above expressions when the same character repeats in the text, we need to use "\" - back slash.

# import re   ### To use any of the above regular expressions.

# s = 'h elloooo hello'
# a = re.search(r'^h\s\w',s)

# if a:
# 	print a.group()

# s = 'you?'
# a = re.search(r'you\?',s)  ### Using ? we should include '\' since it has a meaning in default case 

# if a:
# 	print a.group()


# # Compile and Match

# a = re.compile('you\?')
# b = a.match(s)
# if b:
# 	print b.group()