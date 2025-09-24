# tuple is a collection datatype , which is used to store the multiple values in a single variable
# tuple is a ordered , immutable,also allows the duplicate values, and can store mixed dat type in values.

#example:
# coordinate = ("x","y")
# my_tuple = (10,20,30)
# print(my_tuple)
# print(type(my_tuple))


#creating a tuple 
#empty tuple
# et=()

# tuple with single elment:

# a =10#int
# print(type(a))
# b = [10] #list
# print (type(b))
# c = (10,)#tuple
# print(type(c))


# accessing elements :

# tuple uses index values to access an element 
a = (10,20,30,40)
#i =  0  1  2  3
# print(a[0])#10
# print(a[1])#20
# print(a[2])#30
# print(a[3])#40

# print(a[-1])# 40 
# print(a[-2])#30
# print(a[-3])#20
# print(a[-4])#10

#slicing the tuple :
# extracts part of the tuple using start index and end index 
# ([start index: end index])
# in tuple it will print before the end index ValueError

# A= (10,20,30,40,)
#i = 0 1  2  3
#-i=-4 -3 -2 -1
# print (A[1:3])
# print(a[:2])
# print(A[3:-1])

#changing the val;ues :
#tuple are iimuatble , so we cannot change the values 
# a[1] = 50 
# print (A) #typeerror :  'tuple'object dos not support item assignment
# #append():
# A.append(50)
# print(A)


#length:
# max:
# min:
# concatination:
# repetation:

# searching and checking:
# in operator:
# not in operators:
# index():
# count():

