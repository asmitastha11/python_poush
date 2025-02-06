# # a = 10
# # b = 5
# # i = a+b
# # print(i)

# # x = "mind"
# # y = "risers"
# # j = x+y
# # print(j)

# class Dog:
#     def move(self):
#         return "Dog is walking"
# class Bird:
#     def move(self):
#         return "Bird is flying"
# class Fish:
#     def move(self):
#         return "Fish is swimming"
    
# dog = Dog()
# bird = Bird()
# fish = Fish()

# print(dog.move())
# print(bird.move())
# # print(fish.move())

# todo:
# class named person, attributes name and age, method introduction
# class name student, it inherits person class attributes class and roll no. , method get_class_roll
# create object of student class , print out introduction with class and roll no.


class person:
    name = None
    age = None
    def get_intro(self,name,age):
        self.name = name
        self.age = age
        # print(f"Name:\t{name}\nAge:\t{age}")
class student(person):
    classroom = None
    roll_no = None
    def get_class_roll(self,classroom,roll_no):
        self.classroom = classroom
        self.roll_no = roll_no
        # print(f"Grade:\t{classroom}\nRoll no.:\t{roll_no}")
    
print("\n")
person1 = person()
student1 = student()
person1.get_intro("Asmita","20")
student1.get_class_roll("12","25")
print("Name:\t",person1.name)
print("Age:\t",person1.age)
print("Grade:\t",student1.classroom)
print("Roll no:",student1.roll_no)
print("\n")
person2 = person()
student2 = student()
person2.get_intro("Ram","20")
student2.get_class_roll("12","12")
print("Name:\t",person2.name)
print("Age:\t",person2.age)
print("Grade:\t",student2.classroom)
print("Roll no:",student2.roll_no)

 