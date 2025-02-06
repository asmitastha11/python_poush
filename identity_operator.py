#It compares if the data are same or not(memory location)
# is operator - output true if both the variables are same
# a=10
# b=15
# print(id(a))
# print(id(b))
# print(a  is b)
# is not operator - output true if both the variables are not same
# print(a is not b)
# 9814791171

a= ['a','b', 'c']
b= ['a','b', 'c'] #it checks all the member wether it is matched with variable a or not
print(a in b)