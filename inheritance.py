# 4 
# inheritance - need parent and child class
# parent class should be defined inside the paranthesis of the child class
# child class can use attributes and methods of the parent class, it can have its own attributes and methods
#parent class methods and attributes can be overridden in the child class
class car:
    model = None
    color = None
    
    def get_car_details(self,model,color):
        self.model = model
        self.color = color
c1 = car()
c1.get_car_details("Toyota","silver")
print(c1.model)
print(c1.color)

class EV(car):#Here Ev is child class and car is parent class
    speed = None
    def get_speeed(self,speed):
        self.speed = speed
    def get_car_details(self, model):
        self.model = model
ev1 = EV()
ev1.get_car_details("ABC")
print(ev1.model)
#This is possible.Why?- as it seek on its class if it didnt get anything then it will go and seek in parent class
ev1.get_speeed("200")
print(ev1.speed)