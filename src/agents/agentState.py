
from copy import copy, deepcopy
from util import toVector, printSnow
class AgentState:
    def __init__(self, gameState=None):
        if gameState is not None:
            self.location = gameState.startPoint #TODO this is a gross way of doing this
            self.fuel = 40
            self.salt = 40
            self.snow = deepcopy(gameState.mapData.getSnow())
            self.home = list(gameState.mapGraph.get_map())[0]
            self.snow = deepcopy(gameState.mapData.getSnow())
            self.fuel, self.salt = gameState.agentParams
            self.fuel_capacity, self.salt_capacity = gameState.agentParams

        else:
            self.location = None
            self.fuel = None
            self.salt = None
            self.snow = None
            self.home = None
            self.fuel_capacity = 0
            self.salt_capacity = 0

    def driveTo(self, endPoint):
        direction, length = toVector(self.location, endPoint)
        #iterate state
        self._updateSnow(self.location, endPoint)
        if endPoint == self.home:
            self.fuel = self.fuel_capacity
            self.salt = self.salt_capacity
        else:
            self.fuel = self.fuel - length
        self.location = endPoint

    def __str__(self):
        return str(self.location) + str(self.fuel) + str(self.salt) + str(self.snow)

        #self.salt = amount of snow cleaned

    #erases the snow that the plow passes through
    def _updateSnow(self, start, end):
        #printSnow(self.snow)
        count = 0
        x0, y0 = start
        x1, y1 = end
        if y0 == y1:    #east west
            for i in range(min(x0, x1),max(x0, x1) + 1):
                if self.snow[i][y0] and self.salt > 0:
                    self.salt -= 1
                    self.snow[i][y0] = False
                #print("erasing Snow east west")
        elif x0 == x1:    #north south
            for i in range(min(y0, y1),max(y0, y1) + 1):
                if self.snow[x0][i] and self.salt > 0:
                    self.salt -= 1
                    self.snow[x0][i] = False
                #print("erasing Snow north south")



    def __deepcopy__(self, memodict={}):
        copy = AgentState()
        copy.location = self.location
        copy.fuel = self.fuel
        copy.salt = self.salt
        copy.snow = deepcopy(self.snow)
        copy.home = self.home
        copy.fuel_capacity = self.fuel_capacity
        copy.salt_capacity = self.salt_capacity
        return copy


    #over load == operator
    def __eq__ (self, state):
        if self.location != state.location:
            return False
        if self.fuel != state.fuel:
            return False
        if self.salt != state.salt:
            return False
        for i in range(0, len(self.snow)):
            if self.snow[i] != state.snow[i]:
                return False
        return True
