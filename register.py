# ask user (login or register)
# if register, ask for username and password, store username it in a file
# if login, ask for username and password, and check if the username exist in the file, 
# if yes print login, if not print something
while True:
    ask_user = input("Do you want to login or register or exit? ")
    if ask_user == "register":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        a = open('file.txt','a')
        a.write( username + '\n' )
        a.close()
        print("You have been registered successfully")
    elif ask_user == "login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            b = open('file.txt','r')
            if username  and password in b.read():
                print("Login successful")
            else:
                print("Invalid username or password")
        except:
            print("Invalid username or password")
    elif ask_user == "exit":
        print("Thank you")
        break
    else:
        print("Invalid choice")
