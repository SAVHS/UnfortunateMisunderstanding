from panda3d.core import *

class GroundObject():
	def __init__(self, pos, modelName, modelAnims, health, damage, colliderName, maxHealth, maxSpeed):
        self.actor = Actor(modelName, modelAnims)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)

        self.maxHealth = maxHealth
        self.health = maxHealth
        
        self.damage = damage
        
        self.maxSpeed = maxSpeed

        self.velocity = Vec3(0, 0, 0)
        self.acceleration = 300.0

        

        colliderNode = CollisionNode(colliderName)
        colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.3))
        self.collider = self.actor.attachNewNode(colliderNode)
        self.collider.setPythonTag("object", self)


    def alterHealth():
        if self.health > self.maxHealth:
            self.health = self.maxHealth



class FlyingObject():
    pass
