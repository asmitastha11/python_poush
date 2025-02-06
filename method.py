#string
# a = 'Hello World'
# print(a.capitalize())
# print(a.count('l'))
# print(a.split("l"))


#list
# a = ['a','b','c','d','e']
# a.append('Abc')
# b = a.count('a')
# c = a.index('b')
# print(a)
# print(c)
# print(b)

#set
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# c = a.intersection(b)
# a.intersection_update(b)
# d = a.difference(b)
# a.difference_update(b)
# e = a.union(b)
# print(c)
# print(d)
# print(e)

#dictionary
# a = {1:'Ram', 2:'shyam', 3:'hari'}
# b = a.get(2)
# c = a.values()
# d = a.items()
# print(b)
# print(c)
# print(d)

a = {"asmitastha11":"Baluwatar","someone11":"Someone"}
b = input("Enter your username: ")
c = input("Enter password: ")
if b in a and a[b] == c:
    print("Welcome")
else:
    print("Invalid username and password")