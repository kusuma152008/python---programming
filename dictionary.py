# #dictionary :
#  dictionary is a in-built datatypes,which is used to satore multiplr vaules in a single variable 
# dictionary stores the data in the form of key valuepairs
# each keys is unique and work as an index to access its corresponding values 
# keya are immutable (can't be changed once created),while values can be anything (mutable)
# dictionays are ordered ( from python 3.7+ version) mutable do not allows duplicate keys.KeyboardInterrupt.
# #sytntax
# my_dict = {
#     "key1":"values1"
#     "key2" : "values2"
# "keys3" : "values3"
# "key4" : "values4"

# print(my_dict)
# charcterisitics of dictionary
# key value pairs every entery of dictionay's elemnts is a paie:
# key and value set
# {"name" : "nandan"}
# unique keys:
# examples : 
# A = {"n : "nandan","n","anurag"}
# print(A) #"n1" :" anurag "
# keys must be immutable:
# (keys can be valids keys):(integers,float ,String)
# my_dict = {
# 1 :"values1"
#  10.2:"values2"
# "key3" : "values3"
# }"key4" : "values4"
# print(my_dict)
# BioData = {
# "Name":"kusuma"
# "Roll.No": "M1"
# "Branch" :"CSE"
# "Place" : "Medchal"
 
# # square brackets []
# print(BioData["Name"])
# print(BioData["Roll no"])
# print(BioData["Branch"])
# print(BioData["Place"])
# print(BioData["Age"])  age error in 

#using()  methos:

# print(biodata.get("Name"))
# print(biodata.get("Roll no"))
# print(biodata.get("Branch"))
# print(biodata.get("Place"))


# adding and updateing dictionary:
# adding:  you can insert a new key value pair into a dictuionary
# updating : you can update or change thye values using exsited keys in the dictionaryBio data = {
#     "NAME: Anurag"
#     "Roll.No :"5L6"
#     "Branch" : "CSE AIML"
#     "Place" : "Hyderabad"
# }bio data["age"] = 24 #adding the new key and values
# print(BioData)
# BioData["Place"] = "Hyderabad"#cyhqanging or updating the exsisted key's value
# print(BioData)


# Removing in Dictionary :
# Python gives multiple ways to delete items fram a dictionary.
# pop(),popitem(),clear(),del(delete)
 
# BioData = {
# "Name":"Anurag",
# "Roll.No" :"5L6",
# "Branch" : "CSE AIML",
# "Place" : "Hyderabad",
# "Role" : "Charminar_model"
# }

# pop(): removes the key vaklue 
# bio data.pop("ROLL>NO")
# print(biodata)
# popitem(): removes the last inserted item from the dictionary
# bio data.popitem()
# print(biodata)
# del(delete):deletes the key from dictionay 
# del bio data ["branch"]
# print(bio data)
# clear():removes every item from the dictyionay
# biodata.clear()
# print(biuo data)
# ditionbary methods 
# methods alow you to access dictionary data easily .
# keys(),values(),items()

#  BioData = {
# "Name":"Anurag",
# "Roll.No" :"5L6",
# "Branch" : "CSE AIML",
# "Place" : "Hyderabad",
# "Role" : "soft ware "
# }
# key(): it prints only the keys of dictionary
# print (bio data .key())

# values() : it print only the values in dictionary
# print (bio data .values())

# item(): it print only key values in dictionary
# print (bio data .items())

# updating update():
# BioData.update ({"Role" : "Web Developer","Place" : "Hderabad "})
# print(BioData)

#loops for dictionary : 
# for i  in BioData . values():
#     print(i)

L = [10,20,30,40,50,]

# for i in range(0,5):
#     print(L[i])

# for i in L:
#     print(i)

BioData = {
  "Name" : "Sai ram ",
"Roll.No" :"F9",
"Branch" : "CSE AIML",
"Place" : "Hyderabad",
"Role" :"soft ware "

}
# loops to itrate the keys (by default the dicrtionary"s will stores the key values ):
                          
# for  i in :
# print(i)
# loops to iterate the keys using keys()method:
# for i in biodata.keys():
# print(i)BioData
# loops to iterate the values using valuse ()methos:
# for i in biodata.values():
# print(i)
# loops to iterate the items using items () method :
# for i in biodata.items():
# print(i)


#nested tuple:
# T = (10,(20,30),(40,50))
# #i     0   1      2 
# print(T[2][1])


#nested dictionay 

# student = {
# "S1" :{"Name":"Nandhan", "RollNo":"L6"}
# "S2":{"Name":"Anurag", "RollNo":"L7"}
# "S3":{"Name":"Mani","RollNo":"L8"}
# }
# print(student["S1"]["Name"])
# print(student["S2"]["Name"])
# print(Student["S2"]["Name"])
# print(student["S2"]["RolNo"])
# print(Student["S2"]["RollNo"])
# print(Student["S2"]["RollNO"])


