from agent import Agent
import settings as TDS
import fife, random

_STATE_NONE, _STATE_TALK = 0, 1

class Beekeeper(Agent):
	def __init__(self, model, agentName, layer, uniqInMap=True):
		super(Beekeeper, self).__init__(model, agentName, layer, uniqInMap)
		self.state = _STATE_NONE

	def OnActionFinished(self, instance, action):
		self.talk()

	def start(self):
		loc = self.agent.getLocation()
		c = loc.getLayerCoordinates()
		c.x += random.randint(-1, 1)
		c.y += random.randint(-1, 1)
		self.facingLoc = fife.Location()
		self.facingLoc.setLayer(loc.getLayer())
		self.facingLoc.setLayerCoordinates(c)
		self.talk()
	
	def talk(self):
		self.state = _STATE_TALK
		self.agent.act('talk', self.facingLoc, True) # never calls back