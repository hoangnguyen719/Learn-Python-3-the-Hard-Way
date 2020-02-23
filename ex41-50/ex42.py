## Animal is-a object (yes, sort of confusing) look at the end
class Animal(object):
    pass

## Dog is an animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has a __init__ function with parameters self and name
        self.name = name

## cat is an animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has a __init__ function with parameters self and name
        self.name = name

## class Person is an object
class Person(object):
    def __init__(self, name, pet=None):
        ## class Person has __init__ with self and name parameters
        self.name = name
        ## Person has-a pet of some kind
        self.pet = pet

## class Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        ##
        # self.name = name
        super(Employee, self).__init__(name) # run __init__ of parent class reliably
        ## Employee has a salary of some kind
        self.salary = salary

## Fish is an object:
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## Mary is a Person
mary = Person("Mary", satan)

## Mary has a pet which is Satan
# mary.pet = satan
print(mary.pet.name)

## Frank is an Employee
frank = Employee("Frank", 120000)

# Frank has a pet which is Rover
frank.pet = rover
print(frank.name)
## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
