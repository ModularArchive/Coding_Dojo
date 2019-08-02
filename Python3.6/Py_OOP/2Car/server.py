class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print ("Price: " + str(self.price))
        print ("Speed: " + str(self.speed))
        print ("Fuel: " + str(self.fuel))
        print ("Mileage: " + str(self.mileage))
        print ("Tax: " + str(self.tax))

car1 = Car(20000, 27, "Not Full", 12)
car2 = Car(2000, 5, "Not Full", 111)
car3 = Car(1755, 15, "Kind of Full", 55)
car4 = Car(17000, 25, "Full", 72)
car5 = Car(10111, 45, "Empty", 77)
car6 = Car(350, 35, "Empty", 89)
