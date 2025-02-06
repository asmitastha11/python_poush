# Encapsulation - encapsulating method and attributes in a single unit, data hiding
# '__'followed by the attributes or method name is used to hide the data 
# prevents direct access of attributes and methods by objects

class login:
    __email = None
    __password = None
    
    def get_details(self,email,password):
        self.__email = email
        self.__password = password
    def __detail(self):
        return f"{self.__email}-{self.__password}"
    def printout(self):
        a = self.__detail
        print(a)
l1 = login()
l1.get_details("asmitastha484@gmail.com","1234")
# print(l1.__email)
# print(l1.__password)
# l1.printout()
print(l1.printout())