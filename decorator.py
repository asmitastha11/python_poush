# decorator - @followed by the function name is used to define a decorator
# decorator must be placed one step above the function that is to be sent in decorator
# using decorator is a alternative to call a function like [function(other_function)]
# def program(functions):
#     print("Inside Program function")
#     functions()
#     print("Execution completed")
# @function_name
# @program   
# def Hello():
#     print("Hello world")
#     print("Hello world")
#     print("Hello world")
    # print("Hello world")
    
#alternative of program(Hello) is @program def Hello():
# def divide(a,b):
    # if a<b:
    #     a,b = b,a#swapping condition
    # print(a/b)
    
# divide(2,10)
# use decorator to solve this problem, if numerator is smaller than denomenator, 
# print out positive integer should  not be decimal


def divide(function):
    print("Division execution")