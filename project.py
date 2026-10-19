from platform import platform
from pyexpat import model
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

plane = Entity(model="plane", scale=10000000, collider="mesh",
               texture="grass", position=(0, 0, 0))

Sky()

app.run()
