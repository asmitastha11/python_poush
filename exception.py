#exception -error that occurs during the execution of the program ,
# or we can say error raised if it is not similar with users created program

try:
    a = input("Enter any number: ")
    print(a*3)
except NameError:
    print("Hello ")
except ValueError:
    print("Invalid")
