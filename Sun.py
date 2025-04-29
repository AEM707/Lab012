class Sun:
    def __init__(self, name, radius, mass, temp):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = 0.0
        self.y = 0.0

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def __str__(self):
        return f"Sun {self.name}: Mass={self.mass}, Temp={self.temp}, Pos=({self.x}, {self.y})"
