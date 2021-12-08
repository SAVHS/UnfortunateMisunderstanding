from direct.showbase.ShowBase import ShowBase
from direct.actor import Actor
from panda3d.core import WindowProperties

class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)


		properties = WindowProperties()
		properties.setSize(1000, 750)
		self.win.requestProperties(properties)
		self.box = loader.loadModel("models/environment")
		self.box.reparentTo(self.render)
		
game = Game()
game.run()
