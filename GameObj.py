class GroundObject():
	def __init__(self, pos, modelName, modelAnims, health, damage, damageType, targetType, colliderName, speed):
        self.actor = Actor(modelName, modelAnims)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)
        self.health = health
        self.damage = damage
        self.damageType = damageType
        self.speed = speed
        self.targetType = targetType
        colliderNode = CollisionNode(colliderName)
        colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.3))
        self.collider = self.actor.attachNewNode(colliderNode)
        self.collider.setPythonTag("object", self)


    def alterHealth():
        if self.health > self.maxHealth:
            self.health = self.maxHealth


class Tower():
    pass

class FlyingObject():
    pass
