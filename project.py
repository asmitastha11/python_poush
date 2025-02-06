# import json
# def add_balance(username):
#     amount=input("Enter the amount you want to add: ")
#     a={username:amount}
#     json_a = json.dumps(a)
#     f = open('file.txt','a')
#     f.write((json_a+'\n'))
#     f.close()
#     print("Amount added.")
# def check_balance(username):
#     f = open('file.txt','r')
#     a = f.read().split("-")
#     f.close()
#     add = 0
#     for i in a:
#         if i != '':
#             dict_i = json.loads(i)
#             if username in dict_i:
#                 add += int(dict_i.get(username))
#     print(f"Your balance is {add}")
# def withdraw_blance(username):
#     amount=input("Enter the amount you want to withdraw: ")
#     a={username:amount}
#     json_a = json.dumps(a)
#     f = open('file.txt','a')
#     f.write((json_a-'\n'))
#     f.close()
#     print("Amount is withdrawn.")
    

# def register():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     a = {username:password}
#     json_a = json.dumps(a)#convert dict into python json form
#     f = open('file.txt','a')
#     f.write(json_a+'\n')
#     f.close()
    
# def login():
#     is_login = False
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     f = open('file.txt','r')
#     a = f.read().split("-")
#     f.close()
#     # list_a = a.split(" ")
#     # print(list_a)
#     for i in a:
#         if i != '':
#             dict_i = json.loads(i)
#             if dict_i.get(username) == password:
#                 print("Login Successful")
#             else:
#                 print("Invalid")
#                 is_login=True
#     if is_login:
#         choice = input('''\
#          1.Add balance
#          2.Check balance
#          3.Withdraw balance
#          >>>''')
#     if choice == "1":
#          add_balance(username)
#     elif choice == "2":
#          check_balance(username)
#     elif choice =="3":
#         withdraw_blance(username)
#     else:
#         print("Invalid operation")
# while True:
#     choice = input("Register/Login: ").lower()
#     if choice == "register":
#         register()
#     elif choice == "login":
#         login()
#     a = input("Do you want to continue:\n(y/n)\t")
#     if a == 'y':
#         continue
#     elif a == 'n':
#         break
   


# cli - command line interface
# Ecommerce program

# register
# login
# usertype= seller, buyer
# seller:
#     product add
#     list your product 
#     delete
# buyer:
#     list all the products
#     buy product
#     billing

# logout

# ask user (login or register)
# if register, ask for username, usertype and password, store username, usertype, password it in a file
# if login, ask for username and password, and check if the username exist in the file and password is correct,
# if the logged in user, usertype is seller, show options(product add (name,quantity, description, price)
#     list your product 
#     delete)
# if the logged in users' usertype is buyer, show options(list product, buy produt, optional:billing)
# login crediential,not match validation error
# in a loop
def user_name():
    print("You are on our home page\nWould you like to login or register")