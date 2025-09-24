 #Function:
# it is a block of code that performs a specific task .
#  it allows us to group instructions together and refuse them whenever we needed.
# instead of writing te same code again and again , we just define a function once and call it whenever required.
# syntax:
# def function_name(parameters):
    #function body code
    # return value #optional
# function_name()

# # example:
# def greet():
#     print("Hello World")

#calling a function:
#  calling a function means telling python to run the code inside a function by using it's name followed by paranthese().
# if the function needs input (parameter),we provide values (argument)inside the paranthese .PendingDeprecationWarning
# when we call a function , python jumps to the function,excutes it's code ,and then come back to continue the program.

# def greet(name,branch ): #function name
    
#     print("Hello World",name,branch)
# greet("kusuma", "CSAI&ML ") #calling a function 

#passing parameters and aguments 

# parameter : a variables declared inside the function defination .
# It's acts like an empty container waiting to receive a value.

#aguments: the actual value we pass into the function when calling it.it fills the empty container (parameter).

# example:
# def greet(name): # name = parameter
#     print("Hello",name)#
# greet("kusuma")

#types of function arguments :

# A. positional arguments:
# def greet(rollno,name):
#     print("Hello",name,"Your roll no is",rollno)
#     greet("L6","Kusuma)

