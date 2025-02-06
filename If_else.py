#It is multi line statement, operates in boolean value, conditional satement
#syntax
# if condition:
#     statement 1

#Requirements
# a = 5
# b = 5
# if a < b:
#     print("B is greater")#intended blocks need to be defined
# elif a == b:
#     print("A and B are equal")
# else:
#     print("A is greater")

# a = input("Enter your name:")
# print(a)
# print(type(a))    

a = int(input("Enter any numbers"))
print(a )
b = int(input("Enter another number:"))
print(b)
if a > b:
    print("A is greater.")
elif a == b:
    print("A and B are equal")
else:
    print("B is greater")