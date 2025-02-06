#Exam mark evaluator
# Ask user to enter the mark
# if mark is greater than 90 and smaller than 100 then print excellent
#if mark is greater than 80 and smaller than 90 then print very good
# if mark is greater than 70 and smaller than 80 then print good
# if mark is greater than 60 and smaller than 70 then print fair
# if mark is greater than 50 and smaller than 60 then print could have done better
# if mark is greater than 40 and smaller than 50 then print pass
# if mark is less than 40 then fail

#using while loop

while True:
    c = input("Enter the subject name: ")
    a = int(input("Enter your marks: "))
    if 90<=a<=100:
       print("Excellent ")
    elif 80<=a<90:
        print("Very Good ")
    elif 70<=a<80:
        print("Good")
    elif 60<=a<70:
        print("Fair")
    elif 50<=a<60:
        print("You could have done better.")
    elif 40<=a<50:
        print("Passed")
    elif a<40:
        print("Failed")
    else:
        print("Invalid number")
        
    b = input("Do you have any other subject to enter the marks? \n(y/n)")
    if b == 'y':
        continue
    elif b == 'n':
        break