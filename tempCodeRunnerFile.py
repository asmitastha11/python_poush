
    name = None
    age = None
    def introduction(self,name,age):
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
    

person1 = person()
student1 = student()
person1.introduction("Asmita","20")
student1.get_class_roll("12","25")