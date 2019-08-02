class Bike(object): #Defining the class Bike and adding properties/attributes to it
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 #Setting starting value for miles to 0
        
    def displayInfo(self):
        print (("Price: ") + str(self.price))
        print (("Max Speed: ") + str(self.max_speed) + ("mph"))
        print (("Miles: ")  + str(self.miles) + ("miles"))

    def ride(self):
        print ("Driving")
        self.miles += 10

    def reverse(self):
        print ("Reversing")
        self.miles -= 5

bike1 = Bike(75,75, 20)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(155,50, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(5,200, 7)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
