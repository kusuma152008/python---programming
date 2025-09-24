#Error Hanbding :
# -> errors are mistakes in program that stop it from working coreectly . 
# -> Exception is a special type of error that occurs while the program is running .
# -> python  provides ways to handle exceptions so that the program doesn't crash suddenly .
#Types of errors : 
# 1. Complie-time Error : (Syntax Error)
#Errors that happen when the code is not wrritten correctly (wrong syntax)
# 2. Logical Error :
#Errors when the program runs but gives wrong output because the logic is wrong .
# 3. Runtime Error :(Exceptions) 
#Errors happen when the program is running .

#Type of exception in python :
# 1. Zero division error 
# 2. value error
# 3. Index error 
# 4. key error 
# 5. type error 
# 6 .file not found error 


# 1. Zero division error : 
#it is an exception which divides a number by zero .
# try:
#     a = int(input("Enter the numerator"))
#     b = int(input("Enter the dinominator"))
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")
    
# try:
#     a = int(input("Enter the numerator"))
#     b = int(input("Enter the dinominator"))
#     c = a//b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")
# try:
#     a = int(input("Enter the numerator"))
#     b = int(input("Enter the dinominator"))
#     c = a%b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

# try:  
    # i = 2 
#     n = int (input("Enter the n values:"))
#     if i%n==0:
#         print("Yes , number is multiple of",n)
#     else: 
#         print("No, number not is multiple of",n)

# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

    #  2. value error:
# It's an exception that gives as invalid value given
# try:

#         rollno =  int(input("enter your rollno:"))

# except ValueError:
#         print("Error:Given value is not in the integer datatype")


# # Index error :

# try:
#         List 