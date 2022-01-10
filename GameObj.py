from panda3d.core import *

class GameObject():
	def __init__(self, pos, modelName, modelAnims, damage, colliderName, maxHealth, maxSpeed):
		self.actor = Actor(modelName, modelAnims)
		self.actor.reparentTo(render)
		self.actor.setPos(pos)

		self.maxHealth = maxHealth
		self.health = maxHealth
		
		self.damage = damage
		
		self.maxSpeed = maxSpeed

		self.target = target

		self.velocity = Vec3(0, 0, 0)
		self.acceleration = 300.0

		colliderNode = CollisionNode(colliderName)
		colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.3))
		self.collider = self.actor.attachNewNode(colliderNode)
		self.collider.setPythonTag("object", self)


	def alterHealth():
		if self.health > self.maxHealth:
			self.health = self.maxHealth

	def cleanup(self):
		if self.collider is not None and not self.collider.isEmpty():
			self.collider.clearPythonTag("object")
			base.cTrav.removeCollider(self.collider)
			base.pusher.removeCollider(self.collider)

		if self.actor is not None:
			self.actor.cleanup()
			self.actor.removeNode()
			self.actor = None

		self.collider = None

class Seeker(GameObject):
	GameObject.__init__(self, Vec3(0, 0, 0), "models/SimpleEnemy/simpleEnemy", 
	{
		"walk": "models/SimpleEnemy/simpleEnemy-walk"
		},
		20, 10, "seeker")
	base.pusher.addCollider(self.collider, self.actor)
	base.cTrav.addCollider(self.collider, base.pusher)

	self.target = self.tower

class Panda(GameObject):
	GameObject.__init__(self, Vec3(4, 0, 0), "models/act_p3d_chan", 
	{
		"run": "models/a_p3d_chan_run"
		},
		30, 10, "panda")
	base.pusher.addCollider(self.collider, self.actor)
	base.cTrav.addCollider(self.collider, base.pusher)

	self.target = self.tower
	
	
