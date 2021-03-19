# How to append an element to a key in Dictionary :
Dict = {"name":[],"email":[],"location":[]};
Dict["name"].append("devika")
Dict["email"].append("vaddidevi06")
Dict["location"].append("pullampet")
print(Dict)
# Accessing elements in Dictionary
print("name:",Dict["name"])
print("email:",Dict["email"])
print("location:",Dict["location"])
#Deleting elements in dictionary:
# del Dict["email"]
# print(Dict)
# Dict.clear()
# print(Dict)
# del Dict
# print(Dict)
# Deleting dictionaries using pop
Dict.pop("name")
print(Dict)
#Appending elements to a dictionary
Dict["name"]=["xyz"]
print(Dict)
# updateing elements in dictionary
Dict["name"]=["abc"]
print(Dict)
# inserting a dictionary
Dict1 = {"firstName" : "Nick", "lastName": "Price"}
Dict["firstName"]=Dict1
print(Dict)


