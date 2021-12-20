# solar_system_3d.py

import matplotlib.pyplot as plt
from vectors import Vector

class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50)
        )
        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)


class SolarSystemBody:
    def __init__(self, solar_system, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.solar_system.add_body(self)

    def move(self):
        self.position = (
            self.position
        )
