import turtle


class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float, x: float, y: float,
                 vel_x: float, vel_y: float, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = x
        self.y = y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape("circle")
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()


    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def get_x_vel(self):
        return self.vel_x

    def get_y_vel(self):
        return self.vel_y

    def set_x_vel(self, new_x_vel):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel):
        self.vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
        self.t.goto(self.x, self.y)


    def __str__(self) -> str:
        return f"Planet {self.name}, mass={self.mass}, x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.name == other.name

def main():
    p1 = Planet
