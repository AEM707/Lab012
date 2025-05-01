import turtle

class Sun:
    def __init__(self, name, radius, mass, temp, x, y):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = 0.0
        self.y = 0.0
        self.t = turtle.Turtle()
        self.t.color("Yellow")
        self.t.shape("circle")
        self.t.goto(self.x, self.y)

    def get_mass(self) -> float:
        return self.mass

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def __str__(self) -> str:
        return f"Sun {self.name}: Mass={self.mass}, Temp={self.temp}, Pos=({self.x}, {self.y})"
