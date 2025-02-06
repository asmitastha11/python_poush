# oop - object oriented programming
# class and objects
# class - structure, blueprint,if we define function inside the class then it is called methods
# objects - after creating class this is created, data created using class,single class have multiple
# objects,variable in class are called attribute, functions in class are called methods
# self takes objects name as argument, it is used for connectivity, every function in class must have self as parameter


# class person:
#     def __init__(self,Name,age):
#         self.Name=Name
#         self.age=age
#     def intro(self):
#         print(f"My name is {self.Name} and my age is {self.age}")# have to keep self on this
#     # name = 'Ram'
#     # age = 25
# person1 = person("Ram","25")#class needs to be called using some variable and it is object
# person2  = person("Shyam","21")
# print(person1.Name)
# print(person1.age)
# print(person2.Name)
# print(person2.age)
# print(person1.intro())
# print(person2.intro())

# create class named car
#car has attribute model and color
#one method 
#2 objects of that class

# class car:
#     def __init__(self,model,color):
#         self.model = model
#         self.color = color
#     def intro(self):
#         print(f"The car model is {self.model} and its color is {self.color}")
 
# car1 = car("Toyota","Silver")   
# car2 = car("Tesla","Navy Blue")
# print(car1.intro())
# print(car2.intro())


#without using constructor
# class car:
#     model = None
#     color = None
#     def intro(self,model,color):
#         c = print(f"The car model is {model} and its color is {color}")
#         return c
 
# car1 = car()   
# car2 = car()
# a = car1.intro("Toyota","Silver")
# b = car2.intro("Tesla","Navy Blue")
# print(a)
# print(b)