#definition of SolarObject class
class SolarObject:
    #initializes class and sets initial state of attributes
    def __init__(self, name, farthest_distance, orbit, spin):
        self.name = name
        self.farthest_distance = farthest_distance
        self.orbit = orbit
        self.spin = spin

    #defines a colonialization method that returns the colonialization potential of a SolarObject
    def colonialization(self):
        return round(6000000000/self.farthest_distance,2)

    #defines a print method that prints a SolarObject in a pre-defined format
    def print_object(self):
        print(f"\n{self.name} is {self.farthest_distance} au from the sun, spins {self.spin}, takes {self.orbit} days to spin around the sun, and has a colonialization potential of {self.colonialization()}.")

    #defines a method called spin that passes
    def spin(self):
        pass

#definition of Planet class
class Planet(SolarObject):
    #inherits all attributes, sets self.spin to "slightly elliptical"
    def __init__(self, name, farthest_distance, orbit, spin = 'slightly elliptical'):
        super().__init__(name, farthest_distance, orbit, spin)

#definition of Comet class
class Comet(SolarObject):
    #inherits all attributes, sets self.spin to "like crazy"
    def __init__(self, name, farthest_distance, orbit, spin = 'like crazy'):
        super().__init__(name, farthest_distance, orbit, spin)

    #changes the inherited print method so that the orbit is printed in years
    def print_object(self):
        print(f"\n{self.name} is {self.farthest_distance} au from the sun, spins {self.spin}, takes {self.orbit / 365.25} years to spin around the sun, and has a colonialization potential of {self.colonialization()}.")


#two planets with roughly correct details
mars = Planet("Mars", 1.666, 687)
earth = Planet("Earth", 1, 365.25)

#two comets with roughly correct details
halley_comet = Comet("Halley's Comet", 34, 27000)
hale_bopp = Comet("Hale-Bopp Comet", 370, 900000)

#prints all four objects
mars.print_object()
earth.print_object()
halley_comet.print_object()
hale_bopp.print_object()