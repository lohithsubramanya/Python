#### Dictionary 
### Everything in dictionary is accessed through key . Hence no indexing and slicing


# emp = [23, 'abc', 374567]

d = {'empid':23,'name':{'name1':'abc','name2':'xyz'},'salary':374567}   #### It is of the format {Key:Value} . Also it accepts only immutable data types as key.(Tuple and Strings but not lists& Dictionaries)

# print d['name']['name2']  ### To print xyz.

# insert

# d['age'] = 35
# print d


# d.setdefault('empid',56)  ### Adds the key and value in case key is not present.
# print d                       ### Doesn't update if the key is already present.

### Update


# d['empid'] = 56 
# print d

## Delete  - Non existant

# del d
# del d['empid']
# print d

# del d['name']['name2']
# print d


### To empty the dictionary

# d.clear()  ## But dictionary still exists
# print d


# d.pop('empid')  ### With pop it is possible to check which element is deleted, not with del
# print d

# a = d.popitem()   #### Randomly deletes an entire key and value
# print a

# print d.keys()  ### Displays all the keys
# print d.values()  ### Displays all the values

# print d.items()  ### Gives out the key value pairs as tuples

a = [1,2,3]

# b = dict.fromkeys(a)  ### Creates a dictionary with the given values as keys and no values
# print b

# b = dict.fromkeys(a,17)  ### Creates a dictionary with the given values as keys and value as 17
# print b

b = ['a','b','c']

# c = dict(zip(a,b))  ### zip is used to convert the list into tuples respectively
# print c

# print d['empid']
# print d.get('age') ### If the key is not present it just shows none(Exception) instead of showing an error

# print d['empid']
# print d.get('age', 'not present') ### Passing the message as not present

# help(dict)

# print d.has_key('empid')  ## Checks if the key is present in the dictionary

# a = d.copy()
# print a

# b = {'age':35,'location':'Bangalore'}
# d.update(b)
# print d