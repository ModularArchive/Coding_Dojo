class Animal(object):
    def __init__(self, name, health):
        self.health = 100
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print ("My name is {} I have {} health".format(self.name, self.health))

animal = Animal("Strawberry", 100)
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

dog = Dog("Lemonade", 150)
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, 170)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print ("I am a Dragon")
        super(Dragon, self).displayHealth()

dragon = Dragon("Nightwing", 170)
dragon.fly().displayHealth()
animal = Animal("Slade", 100)
animal.walk().run().displayHealth()