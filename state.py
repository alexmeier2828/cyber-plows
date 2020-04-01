'''
This class keeps track of in game state
'''



class GameState:
    def __init__(self, mapPng):
        self.mapData = MapData(mapPng)


class MapData:
    def __init__(self, mapPng):
        #map conversion will happen here
        self.snow = [[True, True, False], [True, False, True], [True, False, True]]  #placeholder
        self.road = [[True, True, True], [True, True, True], [True, False, True]]  #placeholder
        self.width = 3
        self.height = 3
