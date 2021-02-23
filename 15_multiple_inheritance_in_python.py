class LandAnimal:
    def walk(self):
        print('walk')


class WaterAnimal:
    def walk(self):
        print('swim')


class Amphibian(LandAnimal, WaterAnimal):
    pass


frog = Amphibian()
# prints -> walk
frog.walk()

"""
In the multiple inheritance scenario, any specified attribute is searched first in the current class. 
If not found, the search continues into parent classes in depth-first, left-right fashion 
without searching the same class twice.
"""
