import turtle
from Planet import Planet
from Solar_system import SolarSystem
from Sun import Sun


class Simulation:
    def __init__(self, Solar_system, width: int, height: int, num_periods: int):
        self.Solar_system = Solar_system
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(width = self.width, height = self.height)
        self.screen.bgcolor("black")
        self.t.clear()

    def run(self):
        self.solar_system.show_planets()
        for a_move in range(self.num_periods):
            self.solar_system.move_planets()
            self.solar_system.show_planets()
        self.freeze()

    def freeze(self):
        self.screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()
    simulation = Simulation(solar_system, 500, 500, 2000)

    the_sun = Sun("SOL", 5000, 1000, 5800, 0 , 0)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 1000, 25, 5.0, 200.0, 20, 0, "blue")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, 1000, 62, 10.0, 125.0, 20, 0, "red")

    solar_system.add_planet(the_sun)



    simulation.run()
