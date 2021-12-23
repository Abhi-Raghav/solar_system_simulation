# simple_solar_system.py


from solar_system_3d import SolarSystem, Sun, Planet


solar_sytem = SolarSystem(400)

sun = Sun(solar_sytem)

planets = (
    Planet(solar_sytem, position=(150, 50, 0), velocity=(0, 5, 5)),
    Planet(solar_sytem, mass=20, position=(100, -50, 150), velocity=(5, 0, 0))
)

while True:
    solar_sytem.calculate_all_body_interaction()
    solar_sytem.update_all()
    solar_sytem.draw_all()
    