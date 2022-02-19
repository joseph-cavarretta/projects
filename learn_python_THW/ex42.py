## Animal is-a object
class Animal(object):

    def __init__(self, type, diet, sizes):
        self.type = type
        self.diet = diet
        self.size = ["small", "medium", "large"]

    def introduce(self):
        print (f"I am a {self.type}, my diet is {self.diet}, and I am {self.size}.")

## class dog is-a instance of animal
class Dog(Animal):

    def __init__(self, name):
        ## class dog is-a animal, that has-a attribute name
        self.name = name
        self.type = "mammal"
        self.diet = "omnivore"
        self.size = "medium"

## class cat is-a instance of animal
class Cat(Animal):

    def __init__(self, name):
        ## class cat is-a animal that has-a attribute name
        self.name = name
        self.type = "mammal"
        self.diet = "carnivore"
        self.size = "medium"

## class person is-a object
class person(object):

    def __init__(self, name, pet, weight):
        ## class person is-a abject that has-a attribute name
        self.name = name
        self.pet = pet
        self.weight = weight

    def introduce(self):
        print (f"My name is {self.name}, I have a {self.pet} pet, and I weight {self.weight} pounds.")


## Employee is-a instance of person
#class Employee(person):

#    def __init__(self, name, salary):
        ## class employee has-a name
#        super(Employee, self).__init__(name)
        ## class employee is-a person that has-a attribute salary
#        self.salary = salary

## class fish is-a object
class Fish(object):

    def __init__(self, type, size):
        self.type = type
        self.size = size

    def introduce(self):
        print (f"I am a {self.type}, and I am {self.size}.")

## class salmon is-a instance of fish
class Salmon(Fish):
    pass

## class halibut is-a instance of fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
Dog.introduce(rover)
## satan is-a cat
satan = Cat("Satan")
Animal.introduce(satan)

## mary is-a person
mary = person("Mary", "Satan", 150)
person.introduce(mary)

## mary has-a pet(satan)
mary.pet = satan

## frank is-a Employee with salary 120000
#frank = Employee("Frank", 120000)

# frank has-a pet
#frank.pet = rover

## flipper is-a fish
flipper = Fish("white", "small")
Fish.introduce(flipper)

## crouse is-a salmon
crouse = Salmon("salmon", "medium")
Fish.introduce(crouse)
## harry is-a halibut
harry = Halibut("white", "large")
Fish.introduce(harry)
