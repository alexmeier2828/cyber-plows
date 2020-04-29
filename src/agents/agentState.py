
from copy import copy, deepcopy
from util import toVector, printSnow
class AgentState:
    def __init__(self, gameState=None):
        if gameState is not None:
            self.location = list(gameState.mapGraph.get_map())[0] #TODO this is a gross way of doing this
            self.fuel = gameState.plow.fuel
            self.salt = gameState.plow.salt
            self.snow = deepcopy(gameState.mapData.getSnow())
        else:
            self.location = None
            self.fuel = None
            self.salt = None
            self.snow = None

    def driveTo(self, endPoint):
        direction, length = toVector(self.location, endPoint)
        #iterate state
        self._updateSnow(self.location, endPoint)
        self.location = endPoint
        self.fuel = self.fuel - length

        #self.salt = amount of snow cleaned

    #erases the snow that the plow passes through
    def _updateSnow(self, start, end):
        printSnow(self.snow)
        x0, y0 = start
        x1, y1 = end
        if y0 == y1:    #east west
            for i in range(min(x0, x1),max(x0, x1) + 1):
                self.snow[i][y0] = False
                #print("erasing Snow east west")
        if x0 == x1:    #north south
            for i in range(min(y0, y1),max(y0, y1) + 1):
                self.snow[x0][i] = False
                #print("erasing Snow north south")



    def __deepcopy__(self, memodict={}):
        copy = AgentState()
        copy.location = self.location
        copy.fuel = self.fuel
        copy.salt = self.salt
        copy.snow = deepcopy(self.snow)
        return copy
