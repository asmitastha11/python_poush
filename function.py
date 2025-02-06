# #function - like variable, it stores block of code,multilined,reusability, clean code
# #syntax:
# # def function_name():
# # def Hello():
# #     print("Hello World")
# #     print("Hello World")
# #     print("Hello World")
    # positional argument - parameter accepts the arguments according to the position
    
    #keyword argument- keyword is used to assign the value when calling the function
# # Hello()
# # print("BREAK")
# # Hello()
# #variable used in functions are parameters
# def student(firstname,lastname,age):
#     print("Hello")
#     print(f"Firstname:{firstname}")
#     print(f"Lastname:{lastname}")
#     print(f"Age:{age}")
# first = "Asmita"
# last = "Shrestha"
# student(first))
# #local and global variable
# glo = 'Global'
# def hello():
#     local = 'abc'
#     print(glo)
    
# hello()
# a = 10
# def add():
#     global a
#     a = a+20
#     print(a*10)
# add()    
#we cant change global variable inside the function
# but we can call global variable inside function then modify it
#default argument
# def student(firstname = "firstname",lastname = "lastname",age = "18"):
#     print("Hello")
#     print(f"Firstname:{firstname}")
#     print(f"Lastname:{lastname}")
#     print(f"Age:{age}")
# student("Asmita","Shrestha",21)


# #args - define by using '*'in front of arguments, to take or can pass multiple of arguments, it list out as a tuple,
# def numbers(*args):
#     print(args)
#     for i in args:
#         print(i)
    
# numbers(18,'ram')

# def adds(*args):
#     a = 0
#     for i in args:
#         a+=i
#     print(a)
# adds(5,20,40,35,65)

# kwargs(keyword arguments)-**used to define kwargs,accepts multiple keyword arguments, it displays in dictionary

# def person(name,address,age,phone):
#     print(name, address, age,phone)
# person(name = "Ram",age =21, phone = 9861842178,address="Baluwatar")


# def person(**kwargs):
#     print(kwargs)
#     for key in kwargs.keys():
#         print(key)
#     print("The values are")
#     for key in kwargs.values():
#         print(key)
# person(name = "Ram",age =21, phone = 9861842178,address="Baluwatar")

# def person(age,*a,**kwargs):
#     print(a)
#     print(f"Age:{age}")
#     print(kwargs)#It prints keyword arguments
# person("25","Asmita","Baluwatar","9861842178",dob = 2004, house = "ktm")




#calculator using function
# def add(a,b):
#     c = a+b
#     return c # return - marks the end of the function
# z = add(10,5)
# y = z*2
# print(y)


def add(a,b):
    c = a+b
    print("The sum is",c)
    return c 
def dif(a,b):
    f = a-b
    print("The difference is ",f)
    return f
def mul(a,b):
    d = a*b
    print("The product is ",d)
    return d
def div(a,b):
    e = a/b
    print("The divison is ",e)
    return e

x = int(input("Enter the numbers: "))
y = int(input("Enter the other number: "))
z = input("Enter the operator: ")
if z == '+':
    add(x,y)
elif z == '-':
    dif(x,y)
elif z == '*':
    mul(x,y)
    
elif z == '/':
    div(x,y)
else:
    print("Invalid Operation")