from direct.showbase.ShowBase import ShowBase

class Game(Showbase):
	def __init__(self):
		Showbase.__init__(self)

		properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        