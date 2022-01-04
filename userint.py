import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

from panda3d.core import TextNode




def incBar(arg):
    bar['value'] += arg
    str(bar['value']) + '%'
    

# Create a frame

# Add button
bar = DirectWaitBar(text="", value=100, pos=(0, 0, .9))
bar.setScale(0.3)


# Run the tutorial
base.run()