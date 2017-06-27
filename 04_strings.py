# s = 'this is a string'
# print s[3]  ## prints 3rd character left  to right

# print s[-1]  ## prints the first character from right to left [Processs - Indexing]

# print s[2:7] ## prints a series of characters in the specified range [Processs - Slicing]

# print s[2:] ## till the end of string

# print s[:8] ## from the beginning to the 7th index

# print s[:] ## prints the complete string

# print s[::-1]  ## for reversing the complete string

### Strings are immutable - Cant be updated, inserted and deleted


# m = 'hello'

# print s+m ### Concatenates

# print m*4 


# s = 'this is a string' 

# print s.capitalize()  ### Changes the first letter of the string to CAPS

# print s.title() ### Capitalizes only the 1st letter of each word , also if there's any other alphabet which is in CAPS, it becomes small

# print s.upper() ## Each alphabet is shifted to upper case

# print s.lower() #### Each alphabet is shifted to lower case

# print s.swapcase() ### Swaps lower to upper and vice versa 

# print s.find('i')  ### Returns the index of the occurance of the 1st mentioned alphabet

# print s.find('i',4,10)  ### Returns the index of the occurance of the 1st mentioned alphabet in the range specified

# print s.rfind('i') ### First occurance of the alphabet in reverse order.

# print s.find('f') ### Returns -1 if there is no specified character in the string



##### Index performs the same function as find but throws error in case we run it for a character which is not present


# print s.index('i')  ### Returns the index of the occurance of the 1st mentioned alphabet

# print s.index('i',4,10)  ### Returns the index of the occurance of the 1st mentioned alphabet in the range specified

# print s.rindex('i') ### First occurance of the alphabet in reverse order.

# print s.index('f') 

# print s.count('i') ## Counts the number of alphabets

# print s.islower()  ### Checks if all the characters of the string are in lower case
# print s.isupper() ### Checks if all the characters of the string are in upper case

# print s.isalpha() ###### Checks if all the characters of the string are alphabets

# print s.isdigit() ### Checks if all the character are numbers

# print s.isalnum() ### Checks if all the character are numbers and alphabets

# print s.isspace()  ## Checks for only spaces

# print s.istitle() ## Checks for title case  -  Only 1st letter CAPS remaining small 

# print s.center(30,'@') ### String would be centered with "@" being appended for the empty spaces 

# print s.ljust(30,'#') ### String to the left and appends # for the remaining places

# print s.rjust(20,'$') ## String to the right and appends $ for the remaining positions

# print s.zfill(25) ### Adds '0' before the string to make it the specified length

# print s.replace('i','@')  ### Replaces all the 'i' with '@'

# print s.partition('is') ### Breaks the string into 3 parts at any point. Finds only the first occurance of the given text

# print s.split('i') ### Breaks the string depending on the character given and omits the corresponding character

# s = '                 this is a string                    '
# print s.strip()   ### Strips off the spaces before and after the alphabets in the string



# s = '                 this is a string&&&&&&&&&&&&&&&&' 
# print s.strip('&')   ### Strips off only "&" before and after the alphabets in the string


# help(str)  ### Gives out all the methods present for string

# print s.startswith('this')
# print s.endswith('ing')

# a = ['a','b','c']
# print ''.join(a)   ### joins all the given characters
# print '-'.join(a) ### Inserts - and joins the characters

# print len(s) ## Prints the length of the string