#Dictionary
Dict = {'Tim':10,'Charlie':7,'Tiffany':8,'Robert':9}
Boys = {'Tim':10,'Charlie':7,'Robert':9}
Girls = {'Tiffany':8}
print(Dict)
print(Dict['Tim'])
# Copying dictionary
x=Dict.copy()
print(x)
# Updating Dictionary
Dict.update({"Sravani":10})
print(Dict)
# Delete Dictionary
del (Dict['Charlie'])
print(Dict)
# Dictionary items()
print("Students Name: %s" % list(Dict.items()))
print("name: %s" % list(Dict.items()))
# if keys already exists
for name in list(Dict.keys()):
    if name in list((Boys.keys())):
        print(True)
    else:
        print(False)
# sorting
name = list(Dict.keys())
print(name)
name.sort()
print(name)
for key in name:
    print("@".join((key,str(Dict[key]))))


