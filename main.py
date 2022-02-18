from panda3d.ai import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.ai import AIWorld
from panda3d.core import WindowProperties
from panda3d.core import Spotlight, DirectionalLight, AmbientLight
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import Vec4, Vec3
from panda3d.core import CollisionTraverser, CollisionBox, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode
from panda3d.core import *
from GameObj import *

class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.cTrav = CollisionTraverser()
		self.pusher = CollisionHandlerPusher()
		self.camera.setPos(0, 0, 40)
		self.camera.setP(-90)
		self.setWindow()
		self.setLighting()
		self.loadWorld()
		self.loadTowers()
		self.setAI()


		wallSolid = CollisionTube(-8.0, 0, 0, 8.0, 0, 0, 0.2)
		wallNode = CollisionNode("wall")
		wallNode.addSolid(wallSolid)
		wall = render.attachNewNode(wallNode)
		wall.setY(8.0)

		wallSolid = CollisionTube(-8.0, 0, 0, 8.0, 0, 0, 0.2)
		wallNode = CollisionNode("wall")
		wallNode.addSolid(wallSolid)
		wall = render.attachNewNode(wallNode)
		wall.setY(-8.0)

		wallSolid = CollisionTube(0, -8.0, 0, 0, 8.0, 0, 0.2)
		wallNode = CollisionNode("wall")
		wallNode.addSolid(wallSolid)
		wall = render.attachNewNode(wallNode)
		wall.setX(8.0)

		wallSolid = CollisionTube(0, -8.0, 0, 0, 8.0, 0, 0.2)
		wallNode = CollisionNode("wall")
		wallNode.addSolid(wallSolid)
		wall = render.attachNewNode(wallNode)
		wall.setX(-8.0)

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
		self.tower.setPos(0, 6, .25)
		towerColliderNode = CollisionNode("tower")
		towerColliderNode.addSolid(CollisionBox(0, 3))

		def incBar(arg):
			bar['value'] += arg
			str(bar['value']) + '%'

		bar = DirectWaitBar(text="", value=100, pos=(-0.025, 0, .62))
		bar.setScale(0.1)

		self.tower2 = loader.loadModel("models/room_industrial")
		self.tower2.reparentTo(render)
		self.tower2.setScale(0.075)
		self.tower2.setPos(0, -6, 0.25)

		self.tower3 = loader.loadModel("models/room_industrial")
		self.tower3.reparentTo(render)
		self.tower3.setScale(0.075)
		self.tower3.setPos(5, -3, 0.25)

		self.tower4 = loader.loadModel("models/room_industrial")
		self.tower4.reparentTo(render)
		self.tower4.setScale(0.075)
		self.tower4.setPos(-5, -3, 0.25)

		self.tower5 = loader.loadModel("models/room_industrial")
		self.tower5.reparentTo(render)
		self.tower5.setScale(0.075)
		self.tower5.setPos(-5, 3, 0.25)

		self.tower6 = loader.loadModel("models/room_industrial")
		self.tower6.reparentTo(render)
		self.tower6.setScale(0.075)
		self.tower6.setPos(5, 3, 0.25)

	
	


game = Game()
game.run()
