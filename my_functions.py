##name is the expected parameter
#def greet(name):
    #return "Hey " + name    
    # print("Hey!")

##invoke/call the function
#greeting = greet("John")
#print(greeting)
#print(greet())
#greet()

#parameters and arguments
#refactoring - tidy up you code and make more efficient

# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " + name

# greeting = greet("John", "Morning")
# print(greeting)

# name_1 = "Jarrod"
# time_of_day_1 = "Afternoon"
# greeting_1 = greet(name_1, time_of_day_1)
# print(greeting_1)


def greet():
    #words only exists in the scope of greet()
    words = "Hey"
    return words

print(greet())