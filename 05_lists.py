#### Lists - Similar to arrays but the major difference is that it can hold elements of different data types as compared to C/C++ or Java

d = [2,3, 5.6, 'dfg' , 45]

# print type(d)

# print d[1]
# print d[-1]
# print d[2:5]

a = [5,6]

# print d+a
# print d*2

#### Lists are mutable as compared to strings .

### insert
# d.append(a)   ### Inserts the elements or lists or tuple as it is at the end of the list.
# print d

# d.extend(a)  ### Can extend only lists and tuples , cannot extend single elements only at the end.
# print d

# d.insert(1, 'new value')   ### Inserts the corresponding value/element in the given index
# print d



#### update

# d[2] = 'updated'
# print d


### delete

# print d   ### Deletes the last element of the list based on index
# d.pop()
# print d

# print d
# d.pop(2)
# print d.pop(2) ### Shows which element is deleted
# print d

# d.remove(5.6)  ### Removes the element based on the value given - Also it always needs a value to remove specifically.
# print d

# del d     ### Deletes the complete list
# print d

# del d[2]  ### Deletes the particular element in the index
# print d

# print d.index(5.6)  ### Shows the 1st occurance of the value
# print d.count(5.6) 


# d = [4,3,'hello',6.7,'abc',23 ]  ### Does not support complex numbers but sorts other datatypes based on value and length
# d.sort() 
# print d
 
# d.sort(reverse=True)         #### Reverse sorts the string 
# print d

# d.reverse()     ### Just reverses the list
# print d

# help(list)


#### Tuple 

# Tuple is immutable

# d = (2,3,4.5,'hello',67)
# print d[0] ## Indexing
# print d[2:4] ## Slicing

# print d.index(4.5)
# print d.count(4.5)

# help(tuple)

# min,max, cmp can be used with both lists and tuple 

# print len(d) ## Length