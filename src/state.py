'''
This class keeps track of in game state
'''
import sys
import os
from enum import Enum
from PIL import Image
from map_parse import MapGraph

class GameState:
    def __init__(self, mapPng):
        self.mapData = MapData(mapPng)
        self.mapGraph = MapGraph(mapPng)
        #mapData = self.mapData
        self.plow = Plow(self.mapData)
        #print("plow done")
        self.done = False
        self.score = 0

    def movePlow(self, instruction):
        position = self.plow.currentPosition
        nextPosition = position
        if  instruction == ActionEnum.WAIT:
            nextPosition = position
        elif instruction == ActionEnum.NORTH:
            if position[1] - 1 >= 0:
                nextposition = (position[0], position[1] -1)

        elif instruction == ActionEnum.EAST:
            if position[0] + 1 < self.mapData.width:
                nextPosition = (position[0] +1, position[1])

        elif instruction == ActionEnum.SOUTH:
            if position[1] + 1 < self.mapData.height:
                nextPosition = (position[0], position[1] +1)

        else: #we are going west
            if position[0] - 1 >= 0:
                nextPosition = (position[0] -1, position[1])

        self.plow.currentPosition = nextPosition
        if self.mapData.mapArray[nextPosition[0]][nextPosition[1]] is TileTypes.SNOW:
            self.mapData.mapArray[nextPosition[0]][nextPosition[1]] = TileTypes.ROAD

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
                    mapList[x][y] = TileTypes.SNOW
                if r != 0 and g != 0 and b == 0:
                    mapList[x][y] = TileTypes.HOME
        return mapList

#Class holds variables for the plow, including homebase, current location, available actions, next positions, salt, and fuel.
class Plow:
    def __init__(self, mapData):
        self.fuel = 20 #dummy value
        self.salt = 20 #dummy value

        self.homeBase = self.findStart(mapData) #Find the position of the home base.
        self.currentPosition = self.homeBase    #At the start, the plow's position is at home base.
        self.actions = self.getActions(self.currentPosition, mapData)
        self.nextPosition = self.getNextPosition(self.currentPosition, mapData)

        # #enter a position to see how Plow changes based on that position.
        # random_position = (3,3)



        self.currentPosition = self.homeBase
        self.actions = self.getActions(self.currentPosition, mapData)
        self.nextPosition = self.getNextPosition(self.currentPosition, mapData)

    def findStart(self, mapData): #find the starting position of the plow.
        #print("find start call")
        width = mapData.width
        height = mapData.height
        home = TileTypes.HOME

        for x in range(0, width):
            for y in range(0, height):
                if mapData.mapArray[x][y] == home:
                    homebase = (x,y)

        return homebase

    def getActions(self, position, mapData):
        x_current = position[0]
        y_current = position[1]
        wall = TileTypes.WALL

        #check if the position entered is a wall. which should not be possible for the plow.
        if mapData.mapArray[x_current][y_current] == wall:
            print("Error: Current position is a wall")
            exit()

        actions = []
        width = mapData.width
        height = mapData.height

        surroundings = [[x_current, y_current -1], #North
                        [x_current +1, y_current], #East
                        [x_current, y_current +1], #South
                        [x_current -1, y_current]] #West

        #check your surroundings and append actions if its valid, otherwise, append None.
        for i in range(4):
            check = surroundings[i]

            #if the surrounding tiles dont exist (position on map edge), append none
            if check[0] > width-1 or check [0] < 0 or check[1] > height-1 or check[1] < 0:
                actions.append(None)

            #if the surrounding tile is a wall, append none
            elif mapData.mapArray[check[0]][check[1]] == wall:
                actions.append(None)

            #if surrounding tile exists, and is not a wall, then append the action.
            else:
                if i == 0:
                    actions.append(ActionEnum.NORTH)
                elif i == 1:
                    actions.append(ActionEnum.EAST)
                elif i == 2:
                    actions.append(ActionEnum.SOUTH)
                elif i == 3:
                    actions.append(ActionEnum.WEST)

        #finally append wait, as waiting is always an action available.
        actions.append(ActionEnum.WAIT)
        return actions

    #funciton does not actions to be passed into it to get next position, only the current position the plow is at.
    #returns a list of the next tile based on the available actions
    def getNextPosition(self, position, mapData):
        nextPositions = []
        current_actions = self.getActions(position, mapData)
        print("Current position: " + str(position))
        print("Current actions: " + str(current_actions))

        for i in range(5):
            #next_position = 0
            if current_actions[i] == None:
                nextPositions.append(None)

            elif current_actions[i] == ActionEnum.WAIT:
                nextPositions.append(position)

            elif current_actions[i] == ActionEnum.NORTH:
                next_position = (position[0], position[1] -1)
                nextPositions.append(next_position)

            elif current_actions[i] == ActionEnum.EAST:
                next_position = (position[0] +1, position[1])
                nextPositions.append(next_position)

            elif current_actions[i] == ActionEnum.SOUTH:
                next_position = (position[0], position[1] +1)
                nextPositions.append(next_position)

            else: #we are going west
                next_position = (position[0] -1, position[1])
                nextPositions.append(next_position)

        return nextPositions


#from parseMap
class ActionEnum(Enum):
  NORTH = 0
  SOUTH = 1
  EAST = 2
  WEST = 3
  WAIT = 4

class TileTypes(Enum):
    WALL = 0
    ROAD = 2
    SNOW = 1
    HOME = 3
