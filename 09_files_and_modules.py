#### Files -- Only for txt

# f = open('test.txt','r')
# result=f.read()   ## Reads the entire file
# print result


# f = open('test.txt','r')
# result=f.read(6)   ### Reads the first 6 characters of the file
# print result

# f = open('test.txt','r')  ### if we use open it will go to the beginning
# result=f.read(4)   ### Reads from the 7th char onwards
# print result

# print f.tell()  ## tells the current cursor position

# f.seek(4,0) ### If 2nd Argument is 0 --> Beginning, 1 --> Current, 2--> End 

# print f.tell()

# # f.close() ### To close the file in python

### Write mode

# f = open('test12345.txt','w')  ### Creates a new file if not created


# f = open('test.txt','w')
# f.write('hello')   ### Overwrites the complete file and takes the value given
# f.close()  


### Append

# f = open('test.txt','a')   ### Cursor points to the end of the data in the file
# f.write(' new value') ### Always appends from the end
# f.close()


# f = open('test.txt','r+')  ### Either have r+ declared here or else open write mode to make changes in the file
# a = f.read()
# a = a.replace(' ','$')
# f.seek(0,0)  ### To seek the cursor back to initial position because read and write starts the position of the cursor from the end.
# f.write(a)
# f.close()

### w+ and a+ at home



#### Modules 


# import newPython

# newPython.func2(4)
# print dir(newPython)  ### Prints the functions created or available in module "newPython"



# Alternate method

# from newPython import *   #### * imports all the functions , we can specify which function/s to import here

# func2('hi')