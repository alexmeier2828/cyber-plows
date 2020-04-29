
from copy import copy, deepcopy
from util import toVector
class AgentState:
    def __init__(self, gameState=None):
        if gameState is not None:
            self.location = gameState.plow.currentPosition
            self.fuel = gameState.plow.fuel
            self.salt = gameState.plow.salt
            self.snow = deepcopy(gameState.getSnow())
        else:
            self.location = None
            self.fuel = None
            self.salt = None
            self.snow = None

    def driveTo(endPoint):
        direction, length = toVector(self.location, endpoint)

        #iterate state
        self._updateSnow(self.location, endpoint)
        self.location = endPoint
        self.fuel = self.fuel - length

        #self.salt = amount of snow cleaned

    #erases the snow that the plow passes through
    def _updateSnow(self, startPoint, endPoint):
        raise NotImplementedError

    def __deepcopy__(self, memodict={}):
        copy = AgentState()
        copy.location = self.location
        copy.fuel = self.fuel
        copy.salt = self.salt
        copy.snow = deepcopy(self.snow)
