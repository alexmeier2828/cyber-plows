class AgentState:
    def __init__(self, gameState=None):
        if gameState is not None:
            self.location = gameState.plow.currentPosition
            self.fuel = gameState.plow.fuel
            self.salt = gameState.plow.salt
            self.snow = gameState.getSnow()
            self.node = gameState.mapGraph.get_map().nodes[0];
        else:
            self.location = None
            self.fuel = None
            self.salt = None
            self.snow = None
            self.node = None
