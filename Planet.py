class Planet:
    def __init__(self, name, radius, mass, distance, x, y, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = x
        self.y = y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.color = color

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

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return f"Planet {self.name}: Pos=({self.x:.2f}, {self.y:.2f}) Vel=({self.vel_x:.2f}, {self.vel_y:.2f})"
