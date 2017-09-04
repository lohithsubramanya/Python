#### Sets  - Does not contain duplicate elements inside it.Sets are mutable

# a = {23,6.7,'hello',(6,7)}  ### Elements inside a set are always immutable
# print a

# print a[0]  ## Its unordered , hence doesnt support indexing

# help(set)

### Insertion 

# a.add('new value')
# print a 

### For removal


# a.pop()
# print a

# a.remove(23)
# print a

# a.clear()  Clears and gives back an empty set.

# b = a.copy()
# print b



#### Mathematical Operations

# a = {23,6.7,'hello',(6,7)}
# b = {45,23,6.7,'string'}   ### Difference method gives out elements present in 'a' and not in 'b'
# print a.difference(b)
# print a

# a.difference_update(b)  #### Updates and retains the elements which are not present in b, remaining elements are omitted.
# print a

# print a.intersection(b)  ### Elements common in both 'a' and 'b'

# a.intersection_update(b)
# print a

# print a.union(b)   #### Also possible to have a.union(b,c,d) for above mentioned methods also

# a.update(b)
# print a

# a.discard(23)  ### To remove the element. In case there is no specified element, it throws exception.
# print a

# a.remove(23)  ### Just removes the element, throws error in case there's no specified element in th e set.

# print a.isdisjoint(b)  ### Returns TRUE if there are no common elements, FALSE otherwise

# print a.issubset(b)  ### Checks if 'a' is a subset of 'b'

# print a.issuperset(b)  ### Checks if 'b' is a subset of 'a'

# print a.symmetric_difference(b)  ### New set containing all the elements uncommon in both the sets.

# a.symmetric_difference_update(b)
# print a

# s = 'stringgggg'   ### String does not display duplicates.
# print set(s)




##### Generators

def func():
	i = 0
	while True:
		yeild i
		i +=1

## func returns generator object
print func()