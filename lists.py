#collection data types
#list1 = [10,20,30,40,50]
#list1 = [10,20,30,40,50]#inter values
#fruits = ["apple","banana","mango"]#string values
#list2 = [10.1,20.2,30.3,40.4,50.5]#float values 
#list3 = [True,False,True,True]#boolean values
#list4 = [10,20.2,"hello ",True,"False"]#multiple data types values
#output
#print(list2)
#example :0  1  2  3  4 ......n-1
#list1 = (10,20,30,40,50)
#print(list[0])
#print(list1[1])
#print(list1[2])
#print(list1[3])
#print(list1[4])
 #by negative value
 # print (list[-1])
#print(list1[-2])
#print(list1[-3])
#print(list[-4])

#s1c1 = ["prabhas","balayya","pspk","bob","bhai","vijay thalapathy"]
#print(s1c1[:3])
#print(s1c1[:4])
#print(s1c1[-3:])
#print(s1c1[:6])
#Kalkicast =["prabhas","kamal h","amitha bachan","deepika p","ssr"]
#print (Kalkicast)
#Kalkicast.append("disha patani")
#print(Kalkicast)

# insert : adds a single value at the particular position using index       
# KalkiCast.insert (2,"Vijay D")
#print(KalkiCast)

# extending : adds multiple values at once by combing the lists 
#Kalkicast .extend(["Anudeep","Mrunal T","Bujji"])
#print(KalkiCast)

#Kalkicast .extend(["Anudeep","Mrunal T","Bujji"]) 
#Kalkicast.remove ("Murnal T")

#changing the elements :lists are mutable,
#KalkiCast[1] = "Sandeep R V"
#print(KalkiCast)

# 1. concatenation : jions the two lists together in one list 
#a = [1,2]
#b = [3,4]
#c = a+b
#print(c)


# 2. repetition :  repeats the elements of a list multiple times 
#a= [1,2]
#n= int(input("Enter the n value"))
#b= a*n
#print(b)

#searching and checking in operators :
#in operators is the membership operator which returns the true value when the values exists in the value 
#a= [2,4,6,8,10,12,14]
#if 2  in a:
   #print("yes item is present in list")
    #not in operators
   #if 3 not in a:
       #print("3 not in a")
       #print(a.index(8))
       #print(a.count(8))
        
 #count
  #a [2,4,6,8,10,12,14,16] 
  #ct = 0
  #print(a.count(8))#f
  ##print      
# if i == 8:
#     cnt ==cnt+1
#print(cnt)

#sorting
# st = [25,12,5,31,13,18,7,45,8,55,68]
# st.sort()
# print(st)
# st.reverse()
# print(st)
# st1 = [25,8,4,7,10]
# st1.sort(reverse = true)
# print(st1)
# frnd1 = ["A","C","D","B","B","C","C","A","A"]
# frnd2 = frnd1.cop()
# frnd2(2) = "B"
# print(frnd2)
# built in function loops

# print(sum(st))
# print(len(frnd1))
# print(max(st))
# print(min(st))
# a = "hello world to the python programming"
# b = a.split()
# print(b)

# multiple values using input data to the list 
# a = 10,20,30,40,50
# a = int(input("enter the multiple values:")).split()10 20 30 40 50
# print(a)

#traversing a list :
# Accessing the element using a loop
#using for loop
#cars = ["thar","jaguer","audi","bmw"]
#index    0      1         2     3   4    5
# for car in range (0,5)
# print ("cars=",car)


#using index with for loop :
# a = len(cars) #4
# for i in range(0,a)
# print(cars",i,cars[i])
    
 #adding elements using for loop:
#list1 = "thar","jaguer","audi","bmw"
# list1 = []
# n = int (input("enter the number for the list "))
# for i in range (0,n):
#     a = input ("enter the list values:")
#     list1.append(a)
#     print(list1)
#     #give the input values to the lists from 0 to 10
# if i in range (0,10):
#       a = input ("enter the list values")
#       list1.append(a)
# print(list1)

#give the input values to the list from 1 to 10 
# list ()
# n = int(input("enter the number of list values:"))
# for i in range(n):
#   list.append(i)
# print(list)

# sum of the list items = 10 20 30 40 50 without using sum()

# list1 = [10,20,30,40,50]
# sum = 0
# for i in list1:
#     sum = sum + i
#     print(sum)
#  #convert ["p","y","t","h","o","n"]to python
#  #  list1 =["y","t",h","o","n"]
#     word = "p"
# for i in list1:# y t h o n
#  word = word
# print(word)      

#find the maximum and minimum number from list without using max() and min()
# list = [8,6,10,4,2]
# list.sort()
# print(list)


#find the maximum and minimum number from list wthout using max(),min(),sort().

# list = [10,5,3,6,2,4,9,7,8]
# max1 = list[0]
# min1= list[0]
# for num in list:
#     if num > max1:
#        max1 = num
        
#     if num < min :
#         min1 = num
#         print(max1)
#         print(min1)

#searching for an element in a list 
# list1 = [ 2,4,6,8,10,12,14,16,18,20]
# # name = ["mallareddy sir","revanth reddy sir","modi","rahul gandhi"]
# searching_name = input ("enter the name to be found:")
# for i in list1 :
#     if searching_name== i:
#         found = True


#         if found:
#             print("yes")
#         else:
#             print("No")

 #count even and odd numbers

number = [2,4,6,8,10,12,14,16,18,2,7]
#o = 7
#e = 12
# even_cnt = 0
# odd_cnt = 0

# for i in range (len(number)):
#     if number[i]%2 == 0:
#         even_cnt += 1
# else:
#     odd_cnt += 1
#     print("number of even numbers are:",even_cnt)
#     print("number of odd numbers are:",odd_cnt)


# reversing a list without reverse

list1 = [7,10,12,17,18,23,31,45,227,229]
#find =  o, 1, 2 ,3, 4, 5, 6, 7,8 ,9 
l = len(list1)
r_list = []
for i in range (1-1,-1,-1):
    r_list.append(list1[i])
    print(r_list)
    

    #removing all negative numbers using loop
#     numbers = [-56,-9,2,-8,-30,30,45,23,-19,72,-55,-18,7,0]

#     positive_list = []

#     for i in range(len(numbers)):
#         if numbers[i] >=0:
#             positive_list.append(numbers[i])

# print(positive_list)


# multiple each element in  the list 
#  numbers = [56,92,8,30,45,23,45,23,19,72,55,18,7]
# m = int(input("enter the number to be multiplied:"))
# after_multiplication = []
# for i in members:
#     after_multiplication.append(i*m)
#     print(after_multiplication)
