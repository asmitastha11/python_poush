# # file handling
# # read mode('r')
# # open file, open method takes 2 arguments filepath and mode
# f = open('file.txt','r')
# a = f.read()
# print(a)
# f.close()

# #write mode('w')
# f = open('file.txt','w')
# f.write("Mindrisers")
# f.close()

# #append mode('a')
# f = open("file.txt",'a')
# f.write("Hello world")
# f.close()

import json

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    a = {username:password}
    json_a = json.dumps(a)#convert dict into python json form
    # print(json_a)
    f = open('file.txt','a')
    f.write(json_a+'\n')
    f.close()
    
def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        f = open('file.txt','r')
        a = f.read().split("-")
        f.close()
        # list_a = a.split(" ")
        # print(list_a)
        for i in a:
            if i != '':
                 dict_i = json.loads(i)
                #  print(dict_i)
                 if dict_i.get(username) == password:
                     print("Login Successful")
                 else:
                    print("Invalid")
    
choice = input("Do you want to login or register? ").lower()
if choice == "register":
    register()
elif choice == "login":
    login()
else:
    print("Invalid")
        

