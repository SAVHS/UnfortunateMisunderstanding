from panda3d.core import *

class Tower():
    def __init__(self, pos, health, tower="models/room_industrial"):
        self.tower = tower
        loader.loadModel(tower)
