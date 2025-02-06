# Simple calculator
# get 2 number from user 
# get a operator from user(+,-,*,/)
# if operator is + then add two numbers and show the output
# if operator is - then subtract two numbers and show the output
# if operator is * then multiply two numbers and show the output
# if operator is / then divide two numbers and show the output
try:
    a = int(input("Enter any number: \n")) 
    b = int(input("Enter another number: \n"))
    c = input("Enter the operator that you want to use: ")
    if c == '+':
        print("The sum is ",a+b)
    elif c == '-':
        print("The difference is ",a+b)
    elif c == '*':
        print("The product is ",a+b)
    elif c == '/':
        print("The division is ",a+b)
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid number")
# except NameError:
#     print("Invalid Operation")
        