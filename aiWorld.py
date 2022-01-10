def setAI(self):
		# Creating AI World
		self.AIworld = AIWorld(render)

		self.AIchar = AICharacter("seeker", self.seeker, 30, 1, 1)
		self.AIworld.addAiChar(self.AIchar)
		self.AIbehaviors = self.AIchar.getAiBehaviors()

		self.AIchar2 = AICharacter("panda", self.panda, 50, 1, 1)
		self.AIworld.addAiChar(self.AIchar2)
		self.AIbehaviors2 = self.AIchar2.getAiBehaviors()

		self.AIbehaviors.seek(self.target)
		self.AIbehaviors2.seek(self.target2)

		self.seeker.loop("walk")
		self.bot.loop("run")


		# AI World update
		taskMgr.add(self.AIUpdate, "AIUpdate")
		

	# to update the AIWorld
	def AIUpdate(self, task):
		self.AIworld.update()
		return Task.cont