import turtle
from Planet import Planet
from Solar_system import SolarSystem
from Sun import Sun


class Simulation:
    def __init__(self, Solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.solar_system = Solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        self.t = turtle.Turtle()
        self.t.speed(1000000000000000)
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
        the_sun = Sun("SOL", 5000, 1000000000, 5800, 0, 0)
        solar_system.add_sun(the_sun)

        earth = Planet("EARTH", 40.5, 100, 75, 0, 75, 20, 0,  "green")
        solar_system.add_planet(earth)

        mars = Planet("MARS", 40.5, 100, 75, 0, 125, 20, 0,  "red")
        solar_system.add_planet(mars)


        simulation = Simulation(solar_system, 500, 500, 200000)
        simulation.run()

        solar_system.add_sun(the_sun)
        solar_system.add_planet(earth)
        solar_system.add_planet(mars)


        simulation.run()
