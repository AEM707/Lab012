import math
from universal_gravity import UniversalGravity as U

class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []

    def add_sun(self, the_sun):
        self.the_sun = the_sun

    def add_planet(self, new_planet):
        self.planets.append(new_planet)

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def move_planets(self):
        dt = 0.001
        for planet in self.planets:
            # Move planet
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel()
            )

            # Recalculate gravitational force
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            distance = math.sqrt(dist_x**2 + dist_y**2)

            acc_x = U.G * self.the_sun.get_mass() * dist_x / distance**3
            acc_y = U.G * self.the_sun.get_mass() * dist_y / distance**3

            # Update velocity
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)
