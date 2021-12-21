# simple_solar_system.py


from solar_system_3d import SolarSystem, SolarSystemBody


solar_sytem = SolarSystem(400)
body = SolarSystemBody(solar_sytem, 100, velocity=(1, 1, 1))

for _ in range(100):
    solar_sytem.update_all()
    solar_sytem.draw_all()
    