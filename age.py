#ask user for their age
# if user age is greter than or equal to 18, print  they are eligible for license,and ask if they own any 
# vechile or not , if yes print some remarks and if no print somme remarks as well
# if user age is smaller than 18 , print they arenot eligible for license, and esk if they have any drem vechile
#if yes print some remarks and if no print some remark as well



#nested if
a = int(input("Enter your age: "))
if a >= 18:
    print("You are eligible to get the driving license.")
    b = input("Do you own any private vechile? \n (y/n)")
    if b == 'y':
        c = input("Do you have two or four wheeled vechile? ")
        print(f"Hope you will enjoy riding your {c} vechile. \n Enjoy!")
    elif b == 'n':
        print("Hope you will own your vechhile soon!")
    else:
        print("Invalid Response")
else :
    print("You are not eligible to get driving license.")
    d = input("Do you have any dream vechile to ride or drive?\n(y/n) ")
    if d == 'y':
        print("Hope you will buy and enjoy riding your dream vechile when you get your license.")
    elif d == 'n':
        print("Thank you for your response!")
    else:
        print("Invalid Response")