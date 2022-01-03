import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

from panda3d.core import TextNode

# Add some text


textObject = OnscreenText(text="Every day in every way \nI'm getting better and better.", pos=(-0.4, 0), scale=0.07)

agentOrange = loader.loadFont('AgentOrange.ttf')
textObject.setFont(agentOrange)

# Callback function to set  text
def setText():
        bk_text = "Button Clicked"
        textObject.setText(bk_text)



# Run the tutorial
base.run()