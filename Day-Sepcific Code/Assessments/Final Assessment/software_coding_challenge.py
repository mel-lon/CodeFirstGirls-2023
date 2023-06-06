"""
[4.1] - 19 marks
Using the class diagram provided in the assessment, create the classes and subclasses as described
# Red writing denotes new attributes/methods added in that class
# It is expected that any new methods introduced are abstract unless given an exact value.
# If the class has exact or constant values, e.g. most_populous_species, or that warm_blooded is True for mammals
# - this needs to be defined within the class as this should not change.
# Methods need to return their value.
"""


class Animal:
    warm_blooded = None
    most_populous_species = 'ant'

    def default_sound(self):
        return


class Amphibian(Animal):
    warm_blooded = False
    most_populous_species = 'Frog'


class Reptile(Animal):
    warm_blooded = False
    most_populous_species = 'Unknown'


class Bird(Animal):
    warm_blooded = True
    most_populous_species = 'Chicken'
    can_fly = None

    def default_sound(self):
        return 'Squawk'


class Mammal(Animal):
    warm_blooded = True
    most_populous_species = 'Human'


class Horse(Mammal):
    most_populous_species = 'American Quarter Horse'

    def default_sound(self):
        return 'Neigh'



"""
[4.2] - 6 marks
Make an object for each class and print out the most_populous_species and default_sound for each.
"""


# Create objects and print most_populous_species and default_sound

amphibian = Amphibian()
print("Most populous species of amphibian:", amphibian.most_populous_species)
print("Default sound of amphibian:", amphibian.default_sound())

reptile = Reptile()
print("Most populous species of reptile:", reptile.most_populous_species)
print("Default sound of reptile:", reptile.default_sound())

bird = Bird()
print("Most populous species of bird:", bird.most_populous_species)
print("Default sound of bird:", bird.default_sound())

mammal = Mammal()
print("Most populous species of mammal:", mammal.most_populous_species)
print("Default sound of mammal:", mammal.default_sound())

horse = Horse()
print("Most populous species of horse:", horse.most_populous_species)
print("Default sound of horse:", horse.default_sound())