"""
    this file contains the mapView class which displays the graphical
    representation of the map
"""
import tkinter as tk
from state import *

class MapView:
    def __init__(self, parent, gameState):
        self.height = 1028
        self.width = 1028
        self.grid_height = gameState.mapData.height
        self.grid_width = gameState.mapData.width
        print(str(self.grid_height) + "  " + str( self.grid_width))
        self.mapCanvas = tk.Canvas(parent, bg="black" ,height=self.height, width=self.width)
        self.road_sprite = tk.PhotoImage(file=r'../data/sprites/road.gif')

    def draw(self, gameState):

        for x in range(0, self.grid_height):
            for y in range(0, self.grid_width):
                #road layer
                if gameState.mapData.mapArray[x][y] is TileTypes.ROAD:
                    self.mapCanvas.create_image(x*32, y*32, image=self.road_sprite, anchor=tk.NE)

                #snow layer

                #plow layer

                print(x)
        self.mapCanvas.pack()
