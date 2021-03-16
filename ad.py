# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2)
# print(a[x])

#global variable declaration
f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
 print(f)
f = "changing global variable"
someFunction()
print(f)