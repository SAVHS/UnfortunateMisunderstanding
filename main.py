from panda3d.ai import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.ai import AIWorld
from panda3d.core import WindowProperties
from panda3d.core import Spotlight, DirectionalLight, AmbientLight
from panda3d.core import Vec4, Vec3
from panda3d.core import CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode
from panda3d.core import *
#from GameObj import *

class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.camera.setPos(0, 0, 40)
		self.camera.setP(-90)
		self.setWindow()
		self.setLighting()
		self.loadWorld()
		self.loadTowers()
		self.loadSeeker()
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
		self.tower.setPos(0, 6, .25)

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

	def loadSeeker(self):
		# Seeker
		self.seeker = Actor("models/act_p3d_chan", {"run": "models/a_p3d_chan_run"})
		self.seeker.reparentTo(render)
		
		self.seeker.setPos(Vec3(0, 0, 0))
		cNodePanda = self.seeker.attachNewNode(CollisionNode('cnode_panda'))
		cNodePanda.node().addSolid(CollisionSphere(0, 0, 0.8, 0.8))
		cNodePanda.show()
		self.picker = CollisionTraverser()
		self.picker.showCollisions(render)
		self.pq = CollisionHandlerQueue()

		self.pickerNode = CollisionNode('mouseRay')
		self.pickerNP = camera.attachNewNode(self.pickerNode)
		self.pickerNode.setFromCollideMask(BitMask32.bit(1))
		self.seeker.setCollideMask(BitMask32.bit(1))

		self.pickerRay = CollisionRay()
		self.pickerNode.addSolid(self.pickerRay)
		self.picker.addCollider(self.pickerNP, self.pq)

		self.accept("mouse1", self.mouseClick)
		# Target
		self.target = self.tower
		

	def setAI(self):
		# Creating AI World
		self.AIworld = AIWorld(render)

		self.AIchar = AICharacter("seeker", self.seeker, 100, 1, 1)
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

	def mouseClick(self):
		print('mouse click')
		# check if we have access to the mouse
		if base.mouseWatcherNode.hasMouse():

			# get the mouse position
			mpos = base.mouseWatcherNode.getMouse()

			# set the position of the ray based on the mouse position
			self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
			self.picker.traverse(render)
			# if we have hit something sort the hits so that the closest is first and highlight the node
			if self.pq.getNumEntries() > 0:
				self.pq.sortEntries()
				pickedObj = self.pq.getEntry(0).getIntoNodePath()
				print('click on ' + pickedObj.getName())
		
game = Game()
game.run()
