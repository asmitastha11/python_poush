# abstraction - hiding the unnecessary event from the users 
# and only showing the relevant or necessary events to users

class Bike:
    clutch = False
    acc = False
    
    def start(self):
        clutch = True
        acc = True
        return "Bike start"  #clutch and acc are the unnnecessary events when starting the bike so they are hidden
    
b1 = Bike()
print(b1.start())