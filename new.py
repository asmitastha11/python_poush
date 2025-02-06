# Accounting task
#create a dictionary that stores username as key and password as value
# create a dictionary that stores username and amount as key and value respectively
# ask user for username and password, check if it exist in the dictionary 
# if yes ,show them three option (check balance, add balance,withdraw balance)
# if user choice is check print the initial balance
# if add ask user the amount to add and add it with the balance
# if withdraw,, ask the amount, check if the amount is greater than the balance, if the yes break but if no subtract the amount with the balance
# if username and password doesnot match, print some remark


def add(a,b):
    c = a + b
    return c

def diff(a,b):
    d = a-b
    return d
    

user_details = {"asmita":"0000","ram":"1234","shyam":"5678"}
balance = {"asmita":"10000000","ram":"12340000","shyam":"56780000"}
user_name = input("Enter your username: \n")
password = input("Enter password: \n")
if user_name in user_details and user_details[user_name] == password:
    print("login Successful.")
    while True:
        print("Welcome!! \n How can we assist you? ")
        print("1.Check balance \t2.add balance \t3.withdraw balance")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"You have {balance[user_name]}  balance in your account.")
        elif choice == 2:
            c = int(input("Enter the amount that you want to add:\n"))
            balance[user_name] = add(c,int(balance[user_name]))
            print(f"Your current balance is {balance[user_name]}. ")
            
        elif choice == 3:
            w =int(input("Enter the amount that you want to withdraw:\n"))
            if (w<int(balance[user_name])):
                
                print("You can withdraw your amount")
                balance[user_name] = diff(int(balance[user_name]),w)
                print(f"Now you have {balance[user_name]} balance in your account. ")
            else:
                print("Sorry your balance is not sufficient")
        else:
            print("Invalid choice")
        ask = input("Do you want to continue: (y/n)")
        if ask == 'y':
            continue
        elif ask == 'n':
            break
        else:
            print("Invalid choice")
        
else:
    print("Invalid username or password\nPlease try again.")