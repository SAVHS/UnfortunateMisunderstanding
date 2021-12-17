from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor import Actor
from panda3d.ai import AIWorld
from panda3d.core import WindowProperties
from panda3d.ai import *
from panda3d.core import Spotlight, DirectionalLight, AmbientLight
from panda3d.core import Vec4, Vec3

#from GameObj import *

class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.camera.setPos(0, -20, 32)
		self.camera.setP(-60)
		self.setWindow()
		self.setLighting()
		self.loadWorld()
		self.loadTowers()
		self.loadActors()
		self.setAI()

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
		self.world = loader.loadModel("models/Environment/environment")
		self.world.reparentTo(self.render)

	def loadTowers(self):
		self.tower = loader.loadModel("models/room_industrial")
		self.tower.reparentTo(render)
		self.tower.setScale(0.075)
		self.tower.setPos(0, 2, 5)

		self.tower2 = loader.loadModel("models/room_industrial")
		self.tower2.reparentTo(render)
		self.tower2.setScale(0.075)
		self.tower2.setPos(0, -6, 5)

		self.tower3 = loader.loadModel("models/room_industrial")
		self.tower3.reparentTo(render)
		self.tower3.setScale(0.075)
		self.tower3.setPos(4, -3.4, 5)

		self.tower4 = loader.loadModel("models/room_industrial")
		self.tower4.reparentTo(render)
		self.tower4.setScale(0.075)
		self.tower4.setPos(-4, -3.4, 5)

		self.tower5 = loader.loadModel("models/room_industrial")
		self.tower5.reparentTo(render)
		self.tower5.setScale(0.075)
		self.tower5.setPos(-4, 0, 5)

		self.tower6 = loader.loadModel("models/room_industrial")
		self.tower6.reparentTo(render)
		self.tower6.setScale(0.075)
		self.tower6.setPos(4, 0, 5)

	def setAI(self):
		# Creating AI World
		self.AIworld = AIWorld(render)

		self.AIchar = AICharacter("seeker", self.seeker, 100, 0.05, 5)
		self.AIworld.addAiChar(self.AIchar)
		self.AIbehaviors = self.AIchar.getAiBehaviors()

		self.AIbehaviors.seek(self.target)
		self.seeker.loop("run")

		# AI World update
		taskMgr.add(self.AIUpdate, "AIUpdate")

	# to update the AIWorld
	def AIUpdate(self, task):
		self.AIworld.update()
		return Task.cont

	def loadActors(self):
		self.demitri = Actor("")

game = Game()
game.run()
