from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor import Actor
from panda3d.core import WindowProperties
from panda3d.core import Spotlight, DirectionalLight, AmbientLight
from panda3d.core import Vec4, Vec3

class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.camera.setPos(0, -20, 32)
		self.camera.setP(-60)
		self.setWindow()
		self.setLighting()
		self.loadWorld()

	def setWindow(self):
		self.disableMouse()
		properties = WindowProperties()
		properties.setSize(1000, 750)
		self.win.requestProperties(properties)

	def setLighting(self):
		mainLight = DirectionalLight("main light")
		self.mainLightNodePath = self.render.attachNewNode(mainLight)
		self.mainLightNodePath.setHpr(45, -45, 0)
		self.render.setLight(self.mainLightNodePath)

		ambientLight = AmbientLight("ambient light")
		ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
		self.ambientLightNodePath = self.render.attachNewNode(ambientLight)
		self.render.setLight(self.ambientLightNodePath)
		self.render.setShaderAuto()

	def loadWorld(self):
		self.box = loader.loadModel("models/Environment/environment")
		self.box.reparentTo(self.render)
			
game = Game()
game.run()
