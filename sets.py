#sets:
#set is a collection data type which is used to stored multiple values in asingle varaible.
#sets are unordered unindexed , mutable ,and they donot allow duplicate values
#they are useful when you want to store unique elements and performs the mathematical operation like union, intersection , and difference

#syntax:
# my_set = {element1,elements2,elements3}
#characteristics os sets:
# unordered:
#example {1,2,3} and {3,2,1} are considered same set.
# unindexed: you cannot acessset elments by the index like list or tuple .set[1]
# a = {1,2,3}
# print(a[1])
# unique values only : duplicate values are automatically removed from the set 
# a = {1,2,3,3,2,1,1,1,2}
# print(a) #output :  {1, 2, 3}

# # Creating a set 
# s1 = {1,2,3}
# s2 = {10,12.5,"hello",True}
# # empty set :
# s31 = {}
# s3 = set()
# print(type(s3)) #set

# accessing sets :
#  we cannot directly acess an element using index but we acess an element using loops : 
# A = {"Rajinikanth","snake king","upendra"}
# for role in A:
#   print(role)

# ADDING AN ELEMENT IN SETS:

# s = {12,18,20}
# s.add(25)
# s.update([34,29])
# print(s)

# deleting the elment in set:
# remove(): remove the elmenets ,but it give an error if the values is not found in the set 
# s = {12,18,20,25,34,29,25}
# s.remove(26)
# print(S)# {12,18,20,34,29}
# discards():
# s= {12,18,20,25,34,29,25}
# s.discard(26)
# print(s)
#pop(): remove the random element from the set
# s =  {12,18,20,25,34,29,25}
# s.pop()
# print(s)
# #clear(): removes the every element from the set.
# s =  {12,18,20,25,34,29,25}
# s.clear()
# print(s)

# mathematicaloperation in set 
# union "U"="|": prints the all unique values or element  from the both sets.
# a = {1,2,3}
# b = {4,5,6}
# print(a|b) # {1,2,3,4,5,6}

# # Intersection "n" = "&" :
# a = {1,2,3}
# b = {4,5,6}
# print(a & b) # {1,2,3,4,5,6}

# # union
# print("A.union (B)")

# # intersection(B))# {1,2,3,4,5,6}
# print ("A.intersection(B)") # {3,4}

# # Difference 
# print("A.difference(B)")#{1,2}

# # symmetric difference 
# print("A.symmetric difference (B)")#{1,2,5,6}

