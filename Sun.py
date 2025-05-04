import turtle

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float, y: float):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.color("yellow")
        self.t.shape("circle")
        self.t.goto(self.x, self.y)

    def get_mass(self) -> float:
        return self.mass

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def __str__(self) -> str:
        return f"Sun {self.name}, Mass={self.mass}, Temp={self.temp}, x = {self.x}, y = {self.y})"
