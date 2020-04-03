'''
This class keeps track of in game state
'''
import sys
import os
from enum import Enum
from PIL import Image

class GameState:
    def __init__(self, mapPng):
        self.mapData = MapData(mapPng)



#creates a map representation using an image file
class MapData:
    def __init__(self, imageFileName):
        #map conversion will happen here

        self.imageFileName = imageFileName
        self.mapArray = self._parseImageToArray()

        self.width = len(self.mapArray)
        self.height = len(self.mapArray[0])

    def _parseImageToArray(self):
        png = Image.open(self.imageFileName)
        pixels = png.convert('RGB')
        width = pixels.size[0]
        height = pixels.size[1]
        mapList = []

        #initialize to walls
        for x in range(0, width):
            col = []
            mapList.append(col)
            for y in range(0, height):
                mapList[x].append(TileTypes.WALL)


        for x in range(0, width):
            for y in range(0, height):
                #print(pixels.getpixel((x, y)))
                r,g,b = pixels.getpixel((x,y))
                if r == 0 and g == 0 and b == 0:
                    mapList[x][y] = TileTypes.ROAD
                if r != 0 and g != 0 and b == 0:
                    mapList[x][y] = TileTypes.HOME


        return mapList
class TileTypes(Enum):
    WALL = 0
    ROAD = 2
    SNOW = 1
    HOME = 3
